if __name__ == "__main__":
    qtht = {}
    print("nhap danh sach diem QTHT:")
    str = input("Nhap ma sinh vien: ")
    while(str != ""):
        diem = float(input("Nhap diem qtht: "))
        qtht[str] = diem
        str = input("Nhap ma sinh vien: ")
    
    thi = {}
    print("nhap danh sach diem thi: ")
    s = input("Nhap ma sinh vien: ")
    while(s != ""):
        diem = float(input("Nhap diem thi: "))
        thi[s] = diem
        s = input("Nhap ma sinh vien: ")
    
    tongdiem = {}
    for key in set(qtht.keys() | thi.keys()):
        if qtht[key] < 0 or thi[key] < 0:
            tongdiem[key] = 0
        else:
            tongdiem[key] = (qtht[key]*0.4 + thi[key]*0.6)

    for key in tongdiem.keys():
        print(f"{key} : {tongdiem[key]}")
    print("tong diem:", sum(tongdiem.values()))