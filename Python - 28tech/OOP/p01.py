class phanso:
    def __init__(self, tu, mau):
        self.__tu = tu
        self.__mau = mau
    
    def getTu(self):
        return self.__tu
    
    def getMau(self):
        return self.__mau
    
    def gcd(self):
        tu = self.getTu
        mau = self.getMau
        while mau != 0:
            tmp = tu % mau
            tu = mau
            mau = tmp
        return tu
