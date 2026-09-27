vowels = "aeiouAEIOU"
so_nguyen_am = 0
so_phu_am = 0
count = 0
text = input("Nhập vào một chuỗi : ")
for char in text:
    if char.isalpha():
        if char in vowels:
            so_nguyen_am += 1
        else:
            so_phu_am += 1
print("Số nguyên âm trong chuỗi là : ",so_nguyen_am)
print("Số phụ âm trong chuỗi là : ",so_phu_am)