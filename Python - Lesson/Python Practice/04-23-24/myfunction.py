# Câu 1

def alpha(n):
    cnt = 0
    while n != 0:
        cnt += 1
        n = n // 10
    return cnt

def dequy(n):
    if n == 0:
        return 0
    else:
        return 1 + dequy(n // 10)



# Câu 2

from pprint import pprint
hoc_phan = [
    {
        "ma_hp": "TIN3163",
        "ten_dc": "An ninh mạng",
        "so_tin_chi": 3,
        "ngay_duyet": {"date": {"day": 12, "month": 8, "year": 2021}, "time": {"hour": 20, "minute": 10}},
        "ma_gv": "TIN01"
    },
    {
        "ma_hp": "TRD4133",
        "ten_dc": "An toàn lao động trong trắc địa",
        "so_tin_chi": 3,
        "ngay_duyet": {"date": {"day": 20, "month": 5, "year": 2022}, "time": {"hour": 22, "minute": 58}},
        "ma_gv": "DLY01"
    },
    {
        "ma_hp": "TIN4293",
        "ten_dc": "An toàn mạng",
        "so_tin_chi": 3,
        "ngay_duyet": {"date": {"day": 4, "month": 8, "year": 2021}, "time": {"hour": 6, "minute": 42}},
        "ma_gv": "TIN01"
    },
    {
        "ma_hp": "TRD5033",
        "ten_dc": "Anh văn chuyên ngành",
        "so_tin_chi": 3,
        "ngay_duyet": {},
        "ma_gv": "DLY02"
    }
]

def decuong(x, list):
    for item in list:
        if item["ngay_duyet"]["date"]["year"] == x:
            print(item)
def sodecuong(id, list):
    cnt = 0
    for item in list:
        if id == item["ma_gv"] and len(item["ngay_duyet"]) != 0:
            cnt += 1
    return cnt

def sapxep(list):
    list.sort(key=lambda x: x["ten_dc"])
    for item in list:
        print(item)

x = int(input("Nhap vao nam ban muon truy xuat: "))
decuong(x, hoc_phan)

id = input("Nhap vao ma giang vien ban muon truy xuat: ")
print(sodecuong(id, hoc_phan))

print("Danh sach sau khi sap xep la:")
sapxep(hoc_phan)
