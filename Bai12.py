text = list(map(int, input("Nhập danh sách các số nguyên: ").split()))
for i in text:
    if i == max(text):
        text.count(i)
print("Số lớn nhất là :", max(text), " và xuất hiện", text.count(max(text)), "lần")