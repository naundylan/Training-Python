class hocphan:
    def __init__(self, mahp, tendc, sotc, ngayduyet, magv):
        self.mahp = mahp
        self.tendc = tendc
        self.sotc = sotc
        self.ngayduyet = ngayduyet
        self.magv = magv
    def __str__(self):
        return f"{self.mahp} {self.tendc} {self.sotc} {self.ngayduyet} {self.magv}"
    def check(self):
        day, month, year = map(int, self.ngayduyet.split("/"))
        if day < 1 or (month < 1 or month > 12) or year < 1:
            return 0
        dayinmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            dayinmonth[1] = 29
        if day > dayinmonth[month - 1]:
            return 0
        return 1
    def chuanhoa(self):
        return self.tendc.upper().capitalize().strip()
