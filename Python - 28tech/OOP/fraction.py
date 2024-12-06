class phanso:
    def __init__(self, tu, mau):
        self.__tu = tu
        self.__mau = mau
    
    def getTu(self):
        return self.__tu
    
    def getMau(self):
        return self.__mau
    
    def gcd(self):
        tu = self.getTu()
        mau = self.getMau()
        while mau != 0:
            tmp = tu % mau
            tu = mau
            mau = tmp
        return tu
    
    def rutGon(self):
        gcd = self.gcd()
        tu = self.getTu() // gcd
        mau = self.getMau() // gcd
        return phanso(tu, mau)
    
    def __str__(self):
        return f"{self.getTu()}/{self.getMau()}"
    
if __name__ == "__main__":
    tu = int(input("Nhap tu so: "))
    mau = int(input("Nhap mau so: "))
    tmp = phanso(tu, mau)
    print(tmp.rutGon())