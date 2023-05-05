config = {
    'beta1': 0.9,
    'beta2': 0.999,
    'adverserial_D': 2e-5,
    'adverserial_M': 7e-6,
    'non_adverserial_lr': 1e-4,
    'lrAttr': 0.001,
    'IdDiffersAttrTrainRatio': 2,  # 1/3
    'batchSize': 8,
    'R1Param': 14,
    'lambdaID': 205,
    'lambdaL2': 1,
    'lambdaLND': 1.5,
    'lambdaREC': 0.01,
    'lambdaVGG': 2,
    'a': 0.84,
    'use_reconstruction': True,
    'use_id': True,
    'use_landmark': True,
    'use_adverserial': True,
    'train_precentege': 0.95,
    'epochs': 40,
    'use_cycle': True,
    'use_l2': True,
    'use_pre': True
}
GENERATOR_IMAGE_SIZE = 256
