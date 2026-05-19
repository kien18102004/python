def dao_nguoc(n):
    return int(str(n)[::-1])

def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def la_so_than_thien(n):
    m = dao_nguoc(n)
    return ucln(n, m) == 1

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

dem = 0
print("Cac so than thien:")
for i in range(a, b + 1):
    if la_so_than_thien(i):
        print(i, end=" ")
        dem += 1

print("\nSo luong:", dem)