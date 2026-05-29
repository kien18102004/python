# Nhập dữ liệu
dai = float(input("Nhap chieu dai day hinh khoi chu nhat (cm): "))
rong = float(input("Nhap chieu rong day hinh khoi chu nhat (cm): "))
cao = float(input("Nhap chieu cao hinh khoi chu nhat (cm): "))

n = int(input("So luong so le can hien thi: "))

# Tính toán
dien_tich_day = dai * rong
the_tich = dai * rong * cao

# Ký tự unicode
mu2 = "\u00b2"
mu3 = "\u00b3"

# Xuất kết quả
print(f"\nDien tich day hinh chu nhat = {dien_tich_day:.2f} cm{mu2}")
print(f"The tich hinh khoi = {the_tich:.2f} cm{mu3}")

# In n số lẻ đầu tiên
print("\nCac so le dau tien la:")

dem = 0
i = 1

while dem < n:
    print(i, end=" ")
    i += 2
    dem += 1