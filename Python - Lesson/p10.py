def printInfor(id, dictionary):
    print("Thong tin sinh vien la:")
    print(dictionary[id])

def check(id, dictionary):
    return id in dictionary

if __name__ == "__main__":
    print("nhap so luong sinh vien: ", end="")
    numberOfLists = int(input())
    dic = {}
    for i in range(1, numberOfLists + 1):
        print(f"Sinh vien thu {i} la:")
        listInfor = {}
        print("nhap ma sinh vien: ", end="")
        id = input()
        while(check(id, dic)):
            print("Ma sinh vien da ton tai, Vui long nhap ma khac")
            print("nhap ma sinh vien: ", end="")
            id = input()
        listInfor["maSV"] = id
        print("nhap ho ten sinh vien: ", end="")
        fullName = input()
        listInfor["hoten"] = fullName
        print("nhap so dien thoai sinh vien: ", end="")
        phoneNum = input()
        listInfor["sdt"] = phoneNum
        dic[id] = listInfor
    print("nhap ma sinh vien can truy xuat: ", end="")
    tmp = input()
    while(tmp != ""):
        if check(tmp, dic):
            printInfor(tmp, dic)
            print("nhap ma sinh vien can truy xuat: ", end="")
        else:
            print("ma sinh vien khong ton tai, vui long nhap lai!")
        tmp = input()