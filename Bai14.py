text = list(map(int, input("Nhập danh sách số : ").split()))
text_moi = [i for i in text if i > 10]
print(text_moi)