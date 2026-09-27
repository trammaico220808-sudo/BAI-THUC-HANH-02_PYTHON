text = input("Nhập vào một chuỗi : ")
print(len(text))
print("Số lần xuất hiện của mỗi ký tự trong chuỗi là : ")
for i in set(text):
    print(i,":", text.count(i))