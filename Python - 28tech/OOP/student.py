class student:
    def __init__(self, name, birthday, first, second, third):
        self.__name = name
        self.__birthday = birthday
        self.__first = first
        self.__second = second
        self.__third = third
    
    def getName(self):
        return self.__name
    def getBirthday(self):
        return self.__birthday
    def getFirst(self):
        return self.__first
    def getSecond(self):
        return self.__second
    def getThird(self):
        return self.__third
    
    def __str__(self):
        return f"{self.getName()} {self.getBirthday()} {self.total()}"
    
    def total(self):
        return "%.2f" % ((self.__first + self.__second + self.__third) / 3)
    
if __name__ == "__main__":
    name = input("Nhap ho ten: ")
    birthday = input("Nhap ngay sinh: ")
    list = list(map(int, input("Nhap diem ba mon: ").split()))
    tmp = student(name, birthday, list[0], list[1], list[2])
    print(tmp)