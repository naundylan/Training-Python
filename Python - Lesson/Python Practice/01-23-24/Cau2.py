def dtb(qtht, thi):
    dic = {}
    for masv in set(qtht.keys()).union(thi.keys()):
        qtht_diem = qtht.get(masv, 0)
        thi_diem = thi.get(masv, 0)
        if qtht_diem > 0 and thi_diem > 0:
            dic[masv] = (qtht_diem * 0.4 + thi_diem * 0.6)
        else:
            dic[masv] = 0
    return dic

if __name__ == "__main__":
    qtht = {"23T1020054" : 8.4, "23T1080009" : 2.0, "23T1020012" : 7.9}
    thi = {"23T1020054" : 9.0, "23T1080009": 10, "23T1020375" : 10}
    result = dtb(qtht, thi)
    for key in result.keys():
        print(f"{key} : {result[key]}")
    print("tong diem:", sum(result.values()))