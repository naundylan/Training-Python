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
    
    def __str__(self):
        return f"{self.getId()} {self.getName()} {self.getScore1()} {self.getScore2()} {self.average()}"

if __name__ == "__main__":
    n = int(input("Nhap vao so luong sinh vien: "))
    list = []
    for i in range(n):
        id = input("Nhap vao ID: ")
        name = input("Nhap vao ten sinh vien: ")
        score1 = int(input("Nhap vao diem thu nhat cua sinh vien: "))
        score2 = int(input("Nhap vao diem thu hai cua sinh vien: "))
        s = student(id, name, score1, score2)
        list.append(s)
    print("Danh sach sinh vien la: ")
    for i in range(n):
        print(list[i])