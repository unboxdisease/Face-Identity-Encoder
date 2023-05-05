import torch
import torch.nn as nn
import torch.utils.data
import torchvision
import torchvision.datasets as dset
import torchvision.transforms as transforms


class Inception(nn.Module):
    def __init__(self, full_inception=None):
        super(Inception, self).__init__()
        if full_inception is None:
            full_inception = torchvision.models.resnet18(pretrained=True)
            full_inception.aux_logits = False
            removed = list(full_inception.children())[:-1]
        else:
            removed = list(full_inception.children())

        self.model = nn.Sequential(*removed)
        self.preprocess = transforms.Compose([transforms.Resize(224),
                                              transforms.CenterCrop(224)])

    def forward(self, data):
        resized_data = self.preprocess(data)
        return self.model(resized_data * 255)
