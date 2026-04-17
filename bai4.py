n = int(input("Nhập số nguyên dương n: "))

max_digit = 0
temp = n

while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
    temp //= 10

print("Số lớn nhất =", max_digit)