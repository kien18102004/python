import math

# a) Số thân thiện
so_than_thien = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

print("a) So than thien:")
for i in range(1, 1000001):
    if so_than_thien(i):
        print(i, end=" ")

# b) Số chính phương
so_chinh_phuong = lambda n: int(math.sqrt(n)) ** 2 == n

print("\n\nb) So chinh phuong:")
for i in range(1, 1000001):
    if so_chinh_phuong(i):
        print(i, end=" ")

# c1) Số đồng nhất dùng all
so_dong_nhat_all = lambda n: all(ch == str(n)[0] for ch in str(n))

print("\n\nc1) So dong nhat dung all:")
for i in range(1, 1000001):
    if so_dong_nhat_all(i):
        print(i, end=" ")

# c2) Số đồng nhất dùng any
so_dong_nhat_any = lambda n: not any(ch != str(n)[0] for ch in str(n))

print("\n\nc2) So dong nhat dung any:")
for i in range(1, 1000001):
    if so_dong_nhat_any(i):
        print(i, end=" ")

# d) Số hoàn thiện
so_hoan_thien = lambda n: \
    n > 1 and \
    sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n

print("\nd) So hoan thien:")
for i in range(1, 10001):
    if so_hoan_thien(i):
        print(i, end=" ")