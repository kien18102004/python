s = input("Nhập chuỗi: ")

# 1. Xoá khoảng trắng đầu cuối
s = s.strip()

# 2. Xoá khoảng trắng dư thừa giữa các từ
while "  " in s:
    s = s.replace("  ", " ")

# 3. Xoá khoảng trắng trước dấu , .
s = s.replace(" ,", ",")
s = s.replace(" .", ".")

print("Chuỗi hoàn chỉnh:")
print(s)