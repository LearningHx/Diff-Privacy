
#from pytorch_lightning import seed_everything
import random
import os
from inspect import isfunction
import torch
import numpy as np
def seed_everything(seed):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

seed_everything(42)

def exists(x):
    return x is not None

def default(val, d):
    if exists(val):
        return val
    return d() if isfunction(d) else d
t = torch.zeros((1,4,64,64))
noise = None
noise = torch.randn_like(t)
seed_everything(42)
asd = torch.randn_like(t)
print(noise[0,0,15,:])
print(asd[0,0,15,:])

