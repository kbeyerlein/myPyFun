#!/usr/bin/env python

# Test program to generate a 2D normal array

import numpy as np
import sys

import matplotlib.pyplot as plt

sys.path.append('../src/')
import myMath

shape=(40,40)

arr=myMath.TwoDNormalArray(shape, np.array([int(shape[0]/2),int(shape[1]/2)]), np.array([3,3]))

plt.imshow(arr, interpolation='nearest')
plt.colorbar()
plt.show()
