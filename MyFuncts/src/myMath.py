'''
Created on Sep 5, 2013

@author: kbeyerle
'''

import numpy as np

def flip(p): 
    return 1 if np.random.random() < p else 0