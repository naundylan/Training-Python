# Lớp TacGia để lưu thông tin tác giả
class TacGia:
    def __init__(self, ten, email, gioi_tinh):
        """
        Khởi tạo thông tin cho tác giả
        Tham số:
            ten (str): Tên tác giả
            email (str): Email của tác giả
            gioi_tinh (str): Giới tính của tác giả
        """
        self.Ten = ten
        self.Email = email
        self.GioiTinh = gioi_tinh

    def __str__(self):
        """Trả về chuỗi mô tả thông tin của tác giả"""
        return f"{self.Ten} ({self.Email}, {self.GioiTinh})"


# Lớp Sach để lưu thông tin sách và danh sách tác giả
class Sach:
    def __init__(self, tieu_de, ds_tac_gia, nxb, gia_ban):
        """
        Khởi tạo thông tin cho sách
        Tham số:
            tieu_de (str): Tiêu đề của sách
            ds_tac_gia (list[TacGia]): Danh sách các tác giả
            nxb (str): Nhà xuất bản
            gia_ban (float): Giá bán của sách
        """
        self.TieuDe = tieu_de
        self.DSTacGia = ds_tac_gia
        self.NXB = nxb
        self.GiaBan = gia_ban

    def __str__(self):
        """Trả về chuỗi mô tả thông tin của sách"""
        tac_gia_str = "; ".join([str(tg) for tg in self.DSTacGia])
        return f"Tiêu đề: {self.TieuDe}\nTác giả: {tac_gia_str}\nNXB: {self.NXB}\nGiá bán: {self.GiaBan} VNĐ"


def tim_sach_theo_tac_gia(danh_sach_sach, ten_tac_gia):
    """
    Tìm sách theo tên tác giả
    Tham số:
        danh_sach_sach (list[Sach]): Danh sách các sách
        ten_tac_gia (str): Tên tác giả cần tìm
    Trả về:
        list[Sach]: Danh sách sách có tác giả trùng tên
    """
    ket_qua = []
    for sach in danh_sach_sach:
        for tac_gia in sach.DSTacGia:
            if tac_gia.Ten.lower() == ten_tac_gia.lower():
                ket_qua.append(sach)
                break
    return ket_qua


# Hàm chính
def main():
    # Tạo danh sách tác giả
    tac_gia_1 = TacGia("Bùi Việt Hà", "bvh@example.com", "Nam")
    tac_gia_2 = TacGia("Nguyễn Hoàng Trọng Lộc", "nhtl@example.com", "Nam")
    tac_gia_3 = TacGia("Phạm Thế Long", "ptl@example.com", "Nam")
    tac_gia_4 = TacGia("Bùi Văn Thanh", "bvt@example.com", "Nam")
    tac_gia_5 = TacGia("Ngô Ánh Tuyết", "nat@example.com", "Nữ")
    tac_gia_6 = TacGia("Nguyễn Chí Trung", "nct@example.com", "Nam")
    tac_gia_7 = TacGia("Chung Long Hồ", "clh@example.com", "Nam")
    tac_gia_8 = TacGia("Nguyễn Thanh Hùng", "nth@example.com", "Nam") 

    # Tạo danh sách sách
    sach_1 = Sach(
        "Python cơ bản",
        [tac_gia_1],
        "NXB Đại Học Quốc Gia Hà Nội",
        125000
    )
    sach_2 = Sach(
        "Python – Từ Cơ Bản Đến Giải Đề",
        [tac_gia_2, tac_gia_7, tac_gia_8],
        "NXB Đại Học Sư Phạm Thành Phố Hồ Chí Minh",
        92000
    )
    sach_3 = Sach(
        "Bài Tập Tin Học Dành Cho THCS",
        [tac_gia_3, tac_gia_1, tac_gia_4, tac_gia_5, tac_gia_6],
        "NXB Giáo dục Việt Nam",
        21000
    )

    # Danh sách sách
    danh_sach_sach = [sach_1, sach_2, sach_3]

    # Hiển thị thông tin sách
    print("Danh sách sách:")
    for sach in danh_sach_sach:
        print("-" * 50)
        print(sach)

    # Tìm sách theo tên tác giả
    ten_tac_gia_can_tim = input("\nNhập tên tác giả cần tìm sách: ")
    ket_qua = tim_sach_theo_tac_gia(danh_sach_sach, ten_tac_gia_can_tim)

    # Hiển thị kết quả
    if ket_qua:
        print(f"\nSách của tác giả '{ten_tac_gia_can_tim}':")
        for sach in ket_qua:
            print("-" * 50)
            print(sach)
    else:
        print(f"\nKhông tìm thấy sách nào của tác giả '{ten_tac_gia_can_tim}'.")


if __name__ == "__main__":
    main()
