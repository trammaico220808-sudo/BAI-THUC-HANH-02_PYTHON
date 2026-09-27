text = list(map(int, input("Nhập danh sách các số nguyên: ").split()))
text = list(dict.fromkeys(text))
print(text)