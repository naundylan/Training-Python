class giangvien:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return f"{self.id} {self.name}"
    
class hocphan:
    def __init__(self, id, name, num, datetime, teacherId):
        self.id = id
        self.name = name
        self.num = num
        self.datetime = datetime
        self.teacherId = teacherId
    def __str__(self):
        return f"{self.id} {self.name} {self.num} {self.datetime} {self.teacherId}"
class donvi:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return f"{self.id} {self.name}"
class quanly:
    def __init__(self, gv, hp, dv):
        self.__listGiangvien = gv
        self.__listHocphan = hp
        self.__listDonvi = dv
    def 