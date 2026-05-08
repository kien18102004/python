# iii
S = input("Nhập số điện thoại: ")

kq = []
for i in range(10):
    if str(i) not in S:
        kq.append(i)

print("Các số không xuất hiện là:", kq)