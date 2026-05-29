# Kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


# Đếm số ước
def dem_uoc(n):
    dem = 0

    for i in range(1, n + 1):
        if n % i == 0:
            dem += 1

    return dem


# Liệt kê các ước
def liet_ke_uoc(n):
    print("Cac uoc cua", n, "la:", end=" ")

    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")


# Các số vừa là ước vừa là số nguyên tố
def uoc_nguyen_to(n):
    print("\nCac so vua la uoc cua", n, "vua la so nguyen to la:", end=" ")

    for i in range(1, n + 1):
        if n % i == 0 and la_so_nguyen_to(i):
            print(i, end=" ")
            print() 

# Chạy chương trình

n = int(input("Nhap n: "))

# Kiểm tra số nguyên tố
if la_so_nguyen_to(n):
    print(n, "la so nguyen to")
else:
    print(n, "khong phai la so nguyen to")

# Đếm số ước
print("So uoc cua", n, "la:", dem_uoc(n))

# Liệt kê các ước
liet_ke_uoc(n)

# Các số vừa là ước vừa là số nguyên tố
uoc_nguyen_to(n)