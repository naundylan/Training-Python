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
        "ngay_duyet": {"date": {"day": 3, "month": 4, "year": 2021}, "time": {"hour": 16, "minute": 30}},
        "ma_gv": "DLY02"
    }
]


def namX(list, x):
    return [hp for hp in list if hp["ngay_duyet"]["date"]["year"] == x]
def idfilter(list, id):
    return [hp for hp in list if hp["ma_gv"] == id]
def sapxep(list):
    return sorted(list, key = lambda hp: hp["ten_dc"])

if __name__ == "__main__":
    x = int(input("nhap vao nam can loc ra: "))
    pprint(namX(hoc_phan, x))

    id = input("nhap vao ma giao vien can truy xuat: ")
    pprint(idfilter(hoc_phan, id))

    print()
    print("Danh sach sau khi sap xep la: ")
    print()
    pprint(sapxep(hoc_phan))