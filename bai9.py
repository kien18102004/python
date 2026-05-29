# Nhập chiều dài, rộng, cao
dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))

# Nhập số lượng số lẻ cần hiển thị
so_le = int(input("Số lượng số lẻ cần hiển thị: "))

# Tính diện tích đáy và thể tích
dien_tich = dai * rong
the_tich = dai * rong * cao

# Cách 1
print("Cách 1: Diện tích đáy hình chữ nhật =",
      round(dien_tich, so_le), "cm\u00b2")

print("Cách 1: Thể tích hình khối =",
      round(the_tich, so_le), "cm\u00b3")

# Cách 2
print(f"Cách 2: Diện tích đáy hình chữ nhật = {dien_tich:.{so_le}f} cm\u00b2")

print(f"Cách 2: Thể tích hình khối = {the_tich:.{so_le}f} cm\u00b3")