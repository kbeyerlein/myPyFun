'''
Created on Sep 5, 2013

@author: kbeyerle
'''

import numpy as np

def flip(p): 
    return 1 if np.random.random() < p else 0

def TwoDNormal(x, w, corr=0):
    return np.exp(-1/(2*(1-corr**2))*
           ((x[0]/w[0])**2+
            (x[1]/w[1])**2-
            2*corr*x[0]*x[1]/
            (w[0]*w[1])))/\
            (2*np.pi*w[0]*w[1]*np.sqrt(1-corr**2))

def TwoDNormalArray(shape, mu, sigma, corr=0):
    return np.array([[TwoDNormal(x=np.array([i,j])-mu, w=sigma, corr=corr) for j in range(0,shape[1])]for i in range(0,shape[0])])
