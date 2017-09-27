import os
import sys

import numpy as np
#import pylab as pl
#import matplotlib as mp

def get_array():
   ReprRand = np.empty((1,100))
   np.random.seed(0)
   random = np.random.randn(100)
   ReprRand = np.append(ReprRand,[random],axis=0)
   #repshape = ReprRand.shape
   #print repshape
   return ReprRand


ReprRandAll = np.zeros((50, 2, 100))
for i in range(50):
    ReprRandAll = np.append(ReprRandAll,[get_array()],axis=0)

repshape = ReprRandAll.shape
print repshape
