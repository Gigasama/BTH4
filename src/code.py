# quan_ly_nhan_khau.py

class NhanKhau:
    def __init__(self, ho_ten, tuoi, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.dia_chi = dia_chi

    def __str__(self):
        return f'Họ tên: {self.ho_ten}, Tuổi: {self.tuoi}, Địa chỉ: {self.dia_chi}'


class QuanLyNhanKhau:
    def __init__(self):
        self.danh_sach_nhan_khau = []

    def them_nhan_khau(self, ho_ten, tuoi, dia_chi):
        nhan_khau = NhanKhau(ho_ten, tuoi, dia_chi)
        self.danh_sach_nhan_khau.append(nhan_khau)
        print(f"Đã thêm: {nhan_khau}")

    def xoa_nhan_khau(self, ho_ten):
        self.danh_sach_nhan_khau = [nk for nk in self.danh_sach_nhan_khau if nk.ho_ten != ho_ten]
        print(f"Đã xóa nhân khẩu tên {ho_ten}")

    def hien_thi_nhan_khau(self):
        if not self.danh_sach_nhan_khau:
            print("Không có nhân khẩu nào trong danh sách.")
        else:
            for nk in self.danh_sach_nhan_khau:
                print(nk)


if __name__ == "__main__":
    qlnk = QuanLyNhanKhau()
    while True:
        print("\n1. Thêm nhân khẩu")
        print("2. Xóa nhân khẩu")
        print("3. Hiển thị danh sách nhân khẩu")
        print("4. Thoát")
        chon = input("Chọn chức năng (1/2/3/4): ")

        if chon == '1':
            ho_ten = input("Nhập họ tên: ")
            tuoi = input("Nhập tuổi: ")
            dia_chi = input("Nhập địa chỉ: ")
            qlnk.them_nhan_khau(ho_ten, tuoi, dia_chi)
        elif chon == '2':
            ho_ten = input("Nhập tên nhân khẩu cần xóa: ")
            qlnk.xoa_nhan_khau(ho_ten)
        elif chon == '3':
            qlnk.hien_thi_nhan_khau()
        elif chon == '4':
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
