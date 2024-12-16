import os
curLocation = os.path.dirname(__file__)
os.chdir(curLocation)
class congnhan:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.rank = 0
        self.work = 0
        self.contract = {"day" : 0, "month" : 0, "year" : 0}
    def __init__(self, id, name, rank, work, contract):
        self.id = id
        self.name = name
        self.rank = rank
        self.work = work
        self.contract = {"day" : contract["day"], "month" : contract["month"], "year" : contract["year"]}
    def tienluong(self):
        if self.rank == 1:
            return self.work * 300000
        elif self.rank == 2:
            return self.work * 350000
        elif self.rank == 3:
            return self.work * 400000
    def __str__(self):
        return f"{self.id} {self.name} {self.rank} {self.work} {self.tienluong()} {self.contract["day"]}/{self.contract["month"]}/{self.contract["year"]}"
    def __gt__(self, other):
        if self.contract["year"] == other.contract["year"]:
            if self.contract["month"] == other.contract["month"]:
                return self.contract["day"] > other.contract["day"]
            return self.contract["month"] > other.contract["month"]
        return self.contract["year"] > other.contract["year"]

if __name__ == "__main__":
    with open("CNBac1.txt", "a") as file:
        str = input()
        list = []
        idList = []
        while str != "":
            id, name, rank, work, contract = str.split(", ")
            if id in idList:
                print("Duplicated ID")
                str = input()
                continue
            else:
                idList.append(id)
            contract = contract.split("/")
            contract = {"day" : int(contract[0]), "month" : int(contract[1]), "year" : int(contract[2])}
            new = congnhan(id, name, int(rank), int(work), contract)
            list.append(new)
            str = input()
        list.sort(reverse=True)
        for tmp in list:
            file.write(f"{tmp.id}, {tmp.name}, {tmp.contract["day"]}/{tmp.contract["month"]}/{tmp.contract["year"]}, {tmp.work}, {tmp.tienluong()}\n")
            print(tmp)