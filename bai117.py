n = input("Nhap n: ")

S = 0

for i in range(len(n)):
    for j in range(i, len(n)):
        so_con = int(n[i:j + 1])
        S += so_con ** 2

print("S =", S)