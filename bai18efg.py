# e) Số phong phú
so_phong_phu = lambda n: \
    sum(i for i in range(1, n // 2 + 1) if n % i == 0) > n

print("e) So phong phu:")
for i in range(1, 101):
    if so_phong_phu(i):
        print(i, end=" ")

# f) Số tăng dần
so_tang_dan = lambda n: all(str(n)[i] <= str(n)[i + 1]
                            for i in range(len(str(n)) - 1))

print("\n\nf) So tang dan:")
for i in range(1, 101):
    if so_tang_dan(i):
        print(i, end=" ")

# g) Số Armstrong
so_armstrong = lambda n: sum(int(ch) ** len(str(n))
                             for ch in str(n)) == n

print("\n\ng) So Armstrong:")
for i in range(1, 101):
    if so_armstrong(i):
        print(i, end=" ")