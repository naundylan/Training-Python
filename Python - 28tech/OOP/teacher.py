class person:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__birth = ""
        self.__address = ""
    def __init__(self, id, name, birth, address):
        self.__id = id
        self.__name = name
        self.__birth = birth
        self.__address = address
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getBirth(self):
        return self.__birth
    def getAddress(self):
        return self.__address

class student(person):
    def __init__(self):
        self.__clas = ""
        self.__gpa = 0.0

    def __init__(self, id, name, birth, address, clas, gpa):
        person(id, name, birth, address)
        self.__clas = clas
        self.__gpa = gpa
    def getClass(self):
        return self.__clas
    def getGpa(self):
        return self.__gpa
    
class teacher(person):
    def __init__(self):
        self.__clas = ""
        self.__salary = 0.0
        self.__department = ""
    def __init__(self, id, name, birth, address, department, salary, clas):
        person(id, name, birth, address)
        self.__department = department
        self.__clas = clas
        self.__salary = salary
    def getSalary(self):
        return self.__salary
    def getDepartment(self):
        return self.__department
    def getClass(self):
        return self.__clas
    
if __name__ == "__main__":
    studentList, teacherList = [], []
    classDictionary = {}
    n = int(input())
    for i in range(n):
        id = input()
        if id[:2] == "SV":
            name = input()
            birth = input()
            address = input()
            clas = input()
            gpa = float(input())

            studentList.append(student(id, name, birth, address, clas, gpa))
        elif id[:2] == "GV":
            name = input()
            birth = input()
            address = input()
            department = input()
            salary = float(input())
            clas = input()
            teacherList.append(teacher(id, name, birth, address, department, salary, clas))
    # for i in studentList:
