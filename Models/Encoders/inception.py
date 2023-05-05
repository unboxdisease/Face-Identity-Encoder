import torch
import torch.nn as nn
import torch.utils.data
import torchvision
import torchvision.datasets as dset
import torchvision.transforms as transforms

if __name__=="__main__":
    inception = torchvision.models.inception_v3(pretrained = True)
    data = torch.rand(32,3,299,299)
    inception.aux_logits = False
    res = inception(data)
    logit = res[0]
    print(res)

    print()
    print(logit)

