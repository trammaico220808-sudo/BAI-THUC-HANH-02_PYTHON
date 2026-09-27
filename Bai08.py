danh_sach = list(map(int, input("Nhập danh sách các số nguyên: ").split()))
print("Tổng các số nguyên là :", sum(danh_sach))
print("Trung bình là :", sum(danh_sach)/len(danh_sach))
print("Số lớn nhất là :", max(danh_sach))