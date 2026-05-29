#Hàm kiểm tra số chính phương
so_chinh_phuong = lambda n: int(n**0.5) ** 2 == n


#Hàm kiểm tra số hoàn thiện
so_hoan_thien = lambda n: (
    n > 1 and
    sum(i for i in range(1, n) if n % i == 0) == n
)


#Kết quả

print("Cac so chinh phuong tu 1 -> 10000:")
for i in filter(so_chinh_phuong, range(1, 10001)):
    print(i, end=" ")


print("\n\nCac so hoan thien tu 1 -> 10000:")
for i in filter(so_hoan_thien, range(1, 10001)):
    print(i, end=" ")