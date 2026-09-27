text = list(map(int, input("Nhập danh sách số : ").split()))
so_chan = 0
tong_chan = sum(i for i in text if i % 2 == 0)
print("Tổng các số chẵn là : ", tong_chan)