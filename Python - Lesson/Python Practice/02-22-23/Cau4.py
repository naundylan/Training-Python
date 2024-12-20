import os
from collections import Counter
cur_loca = os.path.dirname(__file__)
os.chdir(cur_loca)
from math import *
class iris:
    def __init__(self, len1, width1, len2, width2, type = None):
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
def docdl(str):
    list = []
    with open(str, "r") as file:
        for line in file:
            if(line.strip()):
                data = line.strip().split(",")
                x1, x2, x3, x4 = map(float, data[:4])
                type = data[4] if len(data) > 4 else "None"
                list.append(iris(x1, x2, x3, x4, type))
    print(len(list))
    return list
def dudoan(list, X, k):
    khoangcach = [(hoa.type, hoa.space(X)) for hoa in list if hoa.type]
    khoangcach.sort(key = lambda x : x[1])
    k_hoa = [type for type, _ in khoangcach[:k]]
    dem = Counter(k_hoa)
    return dem.most_common(1)[0][0]
if __name__ == "__main__":
    file_path = "iris.data"
    list = docdl(file_path)
    print(f"Da doc {len(list)} hoa!")
    X = iris(7.1, 2.8, 6.4, 1.6, None)
    k = 3
    type = dudoan(list, X, k)
    print(f"Kieu du doan cua hoa X la: {type}")