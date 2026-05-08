# iv
S = input("Nhập chuỗi: ")

ds = S.split()
da_gap = []

kq = None
for tu in ds:
    if tu in da_gap:
        kq = tu
        break
    da_gap.append(tu)

print(kq)