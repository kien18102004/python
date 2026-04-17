n = int(input("Nhập số nguyên dương n: "))

temp = n
is_lucky = True

while temp > 0:
    digit = temp % 10
    if digit != 6 and digit != 8:
        is_lucky = False
        break
    temp //= 10

if is_lucky:
    print(n, "là số may mắn")
else:
    print(n, "KHÔNG phải số may mắn")