import numpy as np


def sigmoid_derivative(x):

    k = np.exp(-x)
    j = 1/(1 + k)
    s = j
    ds = s*(1-s)

    return ds

    x = np.array([1, 2, 3])


print("sigmoid_derivative(x) = " + str(sigmoid_derivative(x)))
