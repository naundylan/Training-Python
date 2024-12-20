n = input()
list = []
while(n != ""):
    n = n.split()
    dic = {}
    dic["Ten"] = n[0]
    dic["Soluong"] = int(n[1])
    dic["Giaban"] = int(n[2])
    list.append(dic)
    n = input()
print("Danh sach co so luong be hon 5!")
for i in list:
    if i["Soluong"] < 5:
        print(i["Ten"] + " " + i["Giaban"])
print("Tong tien hang:")
for i in list:
    print(i["Ten"], i["Soluong"] * i["Giaban"])