class student:
    subject = "Python"
    def __init__(self, id, name, score1, score2):
        self.__id = id
        self.__name = name
        self.__score1 = score1
        self.__score2 = score2
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getScore1(self):
        return self.__score1
    def getScore2(self):
        return self.__score2
    def average(self):
        return (self.getScore1() + self.getScore2())/2
if __name__ == "__main__":
    s1 = student("1", "Quyen", 10, 9)
    s2 = student("2", "Alice", 9, 8)
    print(s1.average())
    print(s2.average())