text = input("Nhập vào một chuỗi : ")
def is_palindrome(text):
    return text == text[::-1]

if is_palindrome(text):
    print(text,"là chuỗi đối xứng")
else:
    print(text,"không là chuỗi đối xứng")