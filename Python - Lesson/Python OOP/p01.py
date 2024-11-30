class person:
    #pass khởi tạo class rỗng
    nationlity = "Viet Nam"
    def __init__(self, name, job):
        self.__name = name # private
        self.__job = job # private

    def greet(self):
        print("Xin chao")

    def getName(self):
        return self.__name
    
    def getJob(self):
        return self.__job
    
    def __del__ (self): # Ham huy
        print("Destructor!")

    # def __str__(self):
    #     return f"{self.getName()} {self.getJob()}"

if __name__ == "__main__":
    p1 = person("Quyen", "Dev")
    p2 = person("Alice", "Engineer")
    print(p1.nationlity, p1.getName(), p1.getJob())
    print(p2.nationlity, p2.getName(), p2.getJob())
    p1.greet()
    p2.greet()
    # print(p1.__job) không thể truy cập
    print(p1)
    print(p2.__repr__())




