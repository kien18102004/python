
# Kiem tra so chinh phuong
la_so_chinh_phuong = lambda n: int(n**0.5) ** 2 == n

n = int(input("Nhap n: "))

if la_so_chinh_phuong(n):
    print(n, "la so chinh phuong")
else:
    print(n, "khong phai la so chinh phuong")

# Kiem tra tam giac


kiem_tra_tam_giac = lambda a, b, c: (
    "Khong phai tam giac"
    if a + b <= c or a + c <= b or b + c <= a else

    "Tam giac deu"
    if a == b == c else

    "Tam giac can"
    if a == b or a == c or b == c else

    "Tam giac vuong"
    if a*a + b*b == c*c or
       a*a + c*c == b*b or
       b*b + c*c == a*a else

    "Tam giac thuong"
)

# Nhap 3 canh
a = int(input("\nNhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))


print(kiem_tra_tam_giac(a, b, c))