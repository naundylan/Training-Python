class student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__clas = ""
        self.__birth = ""
        self.__gpa = 0.0

    def __init__(self, id, name, clas, birth, gpa):
        self.__id = id
        self.__name = name
        self.__clas = clas
        self.__birth = birth
        self.__gpa = gpa

    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getBirth(self):
        return self.__birth
    def getClass(self):
        return self.__clas
    def getGpa(self):
        return self.__gpa
    def setBirth(self, birth):
        self.__birth = birth
    
    def format(self):
        if self.getBirth()[1] == '/':
            self.setBirth("0" + self.getBirth())
        if self.getBirth()[4] == '/':
            self.setBirth(self.getBirth()[:3] + "0" + self.getBirth()[3:])
        return self.getBirth()
    def __str__(self):
        return f"{self.getId()} {self.getName()} {self.getClass()} {self.format()} {self.getGpa():.2f}"
    
if __name__ == "__main__":
    student1 = student("12345", "John Doe", "10A", "18/5/2005", 10)
    print(student1)