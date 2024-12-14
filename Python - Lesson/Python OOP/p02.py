import os
print(os.getcwd())
os.chdir(os.path.dirname(__file__))  # Thay đổi thư mục làm việc về vị trí file hiện tại


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
    
with open(r"input01.txt", "r") as file:
    line = file.readlines()
if __name__ == "__main__":
    studentList = []
    for i in line:
        i = i.split(";")
        if i[0] == "":
            break
        studentList.append(student(i[0], i[1], float(i[2]), float(i[3])))
    with open(r"result01.txt", "w") as file:
        for i in studentList:
            file.write(f"{i.getName()} {i.average()}\n")