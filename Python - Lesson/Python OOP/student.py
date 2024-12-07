class student:
    subject = "Python"
    def __init__(self, id, name, birth, score1, score2):
        self.__id = id
        self.__name = name
        self.__birth = birth
        self.__score1 = score1
        self.__score2 = score2
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getBirth(self):
        return self.__birth
    def getScore1(self):
        return self.__score1
    def getScore2(self):
        return self.__score2
    
    def average(self):
        return (self.getScore1() + self.getScore2())/2
    
    def __str__(self):
        return f"{self.getName()} {self.getBirth()} {self.getBirth()} {self.average()}"
    
    def __lt__(self, other):
        return self.average() < other.average()

if __name__ == "__main__":
    n = int(input("Nhap so sinh vien: "))
    l = []
    for i in range(n):
        print(f"Nhap sinh vien thu {i + 1}: ")
        id = input("Nhap id: ")
        name = input("Nhap ten: ")
        tmp = list(map(int, input("Nhap ngay thang nam: ").split()))
        birth = {"Ngay" : tmp[0], "Thang" : tmp[1], "Nam" : tmp[2]}
        score1 = float(input("Nhap diem thu nhat: "))
        score2 = float(input("Nhap diem thu hai: "))
        st = student(id, name, birth, score1, score2)
        l.append(st)
    for i in range(n):
        print(l[i])
