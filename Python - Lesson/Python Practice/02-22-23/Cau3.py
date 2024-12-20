from math import *
class iris:
    def __init__(self, len1, width1, len2, width2, type = "None"):
        self.len1 = len1
        self.width1 = width1
        self.len2 = len2
        self.width2 = width2
        self.type = type
    def setType(self, str):
        self.type = str
    def space(self, other):
        space = sqrt((self.len1 + other.len1)**2 + 
                     (self.width1 + other.width1)**2 + 
                     (self.len2 + other.len2)**2 + 
                     (self.width2 + other.width2)**2)
        return round(space, 2)