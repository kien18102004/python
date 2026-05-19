def tao_strobo(n, mo_rong=False):
    if mo_rong:
        cap = [('0', '0'), ('1', '1'), ('2', '2'), ('5', '5'),
               ('6', '9'), ('8', '8'), ('9', '6')]
        giua = ['0', '1', '2', '5', '8']
    else:
        cap = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
        giua = ['0', '1', '8']

    kq = []

    def de_quy(s, l, r):
        if l > r:
            kq.append(''.join(s))
            return

        if l == r:
            for x in giua:
                s[l] = x
                kq.append(''.join(s))
            return

        for a, b in cap:
            if l == 0 and a == '0':
                continue
            s[l] = a
            s[r] = b
            de_quy(s, l + 1, r - 1)

    s = [''] * n
    de_quy(s, 0, n - 1)
    return kq


n = int(input("Nhap n (2 <= n <= 10): "))

print("a. Cac so strobogrammatic gom", n, "chu so:")
ds1 = tao_strobo(n, False)
for x in ds1:
    print(x, end=" ")

print("\n\nb. Cac so strobogrammatic mo rong gom", n, "chu so:")
ds2 = tao_strobo(n, True)
for x in ds2:
    print(x, end=" ")