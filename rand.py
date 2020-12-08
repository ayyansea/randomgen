import numpy
import random

def even(min, max):
    return float(random.random() * (max - min) + min)

def normal():
    return abs(numpy.random.randn())
