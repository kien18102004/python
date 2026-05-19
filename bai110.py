s = input("Nhap cipher text: ")

kq = ""
i = 0

while i < len(s):
    if s[i] == "#":
        so_lan = int(s[i + 1])
        ky_tu = s[i + 2]
        kq += ky_tu * so_lan
        i += 3
    else:
        kq += s[i]
        i += 1

print("Plain text:", kq)