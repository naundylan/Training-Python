class staff:
    count = 0
    def __init__(self, name, salary, days, position):
        count = count + 1
        self.__id = "NV" + f"{count:.02}"
        self.__name = name
        self.__salary = salary
        self.__days = days
        self.__position = position
    def getSalary(self):
        return self.__salary
    def getDays(self):
        return self.__days
    def getPos(self):
        return self.__position
    def plus(self):
        if self.__position == "GD":
            plus += 250000
        elif self.__position == "PGD":
            plus += 200000
        elif self.__position == "TP":
            plus += 180000
        elif self.__position == "NV":
            plus += 150000
        return plus
    def prize(self):
        total = 0
        if self.__days >= 25:
            total += 0.2
        elif self.__days >= 22:
            total += 0.1
        elif self.__days > 0:
            total += 0
        return total
    def total(self):
        total = self.__salary * self.__days
        plus = self.plus()
        prize = self.prize()        
        return total + plus + prize*total
    
    def __str__(self):
        return f"{self.__id} {self.__name} {self.__salary} {self.prize()} {self.plus()} {self.total()}"
    
if __name__ == "__main__":
    staff1 = staff("Nguyen Van A", 26000, 21, "PGD")