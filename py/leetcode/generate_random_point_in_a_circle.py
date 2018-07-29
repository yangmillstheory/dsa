import math
from random import uniform, random


class Solution(object):
    def __init__(self, radius, x, y):
        self._radius = radius
        self._center = (x, y)

    def randPoint(self):
        r = math.sqrt(random())*self._radius  # want farther out points to be picked more (proportional to circle area)
        theta = uniform(0, 2*math.pi)
        return self._center[0]+(r*math.cos(theta)), self._center[1]+(r*math.sin(theta))
