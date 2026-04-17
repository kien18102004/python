n = int(input("Nhập số nguyên dương n: "))

tong = 0
tich = 1

temp = n  # giữ lại n ban đầu

while temp > 0:
    digit = temp % 10
    tong += digit
    tich *= digit
    temp //= 10

print("Tổng =", tong)
print("Tích =", tich)