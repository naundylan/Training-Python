class teacher:
    def __init__(self, id, name, salary):
        self.__id = id
        self.__name = name
        self.__salary = salary
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def rank(self):
        return int(self.__id[2:])
    
    def total(self):
        position = self.__id[:2]
        rank = self.rank()
        if position == "HT":
            plus = 2000000
        elif position == "HP":
            plus = 900000
        elif position == "GV":
            plus = 500000
        return rank * self.__salary + plus
    def __str__(self):
        return f"{self.getId()} {self.getName()} {self.rank()} {self.total()}"
if __name__ == "__main__":
    teacher1 = teacher(input("Nhap ID: "), input("Nhap ten: "), int(input("Nhap luong co ban: ")))
    print(teacher1)
