from __future__ import division
import numpy as np


class EuclideanLoss(object):
    def __init__(self, name):
        self.name = name

    def forward(self, input, target):
        batch_size = len(input)
        dist = np.sum(np.square(target - input)) / 2
        dist = dist / batch_size
        return dist

    def backward(self, input, target):
        batch_size = len(input)
        grad = input - target
        grad = grad / batch_size
        return grad
        
