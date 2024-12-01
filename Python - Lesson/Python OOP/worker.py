class worker:
    def __init__(self, id, name, rank, workDays, startDay) -> None:
        self.__id = id
        self.__name = name
        self.__rank = rank
        self.__workDays = workDays
        self.__startDay = startDay

    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getRank(self):
        return self.__rank
    def getWorkdays(self):
        return self.__workDays
    def getStartDay(self):
        return self.__startDay

    def money(self):
        rank = self.getRank()
        if rank == 1:
            return 300000
        elif rank == 2:
            return 350000
        else:
            return 400000
        
    def salary(self):
        return self.getWorkdays() * self.money()
    
    def __str__(self):
        return f"{self.getId()} {self.getName()} {self.getRank()} {self.getWorkdays()} {self.salary()}"

if __name__ == "__main__":
    list = []
    str = "tmp"
    while(str != ""):
        str = input("Nhap id: ")
        if str == "":
            break
        if str 
        id = str
        name = input("Nhap ho ten cong nhan: ")
        rank = int(input("Nhap bac cua cong nhan (So nguyen): "))
        workDays = int(input("Nhap so ngay lam viec cua cong nhan (So nguyen): "))
        day = int(input("Nhap ngay: "))
        month = int(input("Nhap thang: "))
        year = int(input("Nhap nam: "))
        date = dict(day = day, month = month, year = year)
        tmp = worker(id, name, rank, workDays, date)
        list.append(tmp)

    print("Danh sach cong nhan sau khi nhap la:")
    for _ in list:
        print(_)
