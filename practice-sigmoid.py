import numpy as np


def sigmoid(x):
  
    k = np.exp(-x)
    s = 1/(1 + k)


    return s

x = np.array([1, 2, 3])
sigmoid(x)
