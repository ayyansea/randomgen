import numpy
import random
import math

def even(min, max):
    return float(random.random() * (max - min) + min)

def normal():
    return abs(numpy.random.randn())

def exp(lam):
    return -1 / lam * math.log(random.random())


