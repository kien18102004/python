N = 1000000

def la_nguyen_to(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def xoay_so(n, mo_rong=False):
    bang = {
        0: 0,
        1: 1,
        6: 9,
        8: 8,
        9: 6
    }

    if mo_rong:
        bang[2] = 2
        bang[5] = 5

    if n == 0:
        return 0

    kq = 0
    while n > 0:
        d = n % 10
        if d not in bang:
            return -1
        kq = kq * 10 + bang[d]
        n //= 10

    return kq


def la_strobo(n):
    return xoay_so(n, False) == n


def la_strobo_mo_rong(n):
    return xoay_so(n, True) == n


print("a. Cac so strobogrammatic < 1 trieu:")
for i in range(N):
    if la_strobo(i):
        print(i, end=" ")

print("\n\nb. Cac so nguyen to strobogrammatic < 1 trieu:")
for i in range(N):
    if la_strobo(i) and la_nguyen_to(i):
        print(i, end=" ")

print("\n\nc. Cac so strobogrammatic mo rong < 1 trieu:")
for i in range(N):
    if la_strobo_mo_rong(i):
        print(i, end=" ")

print("\n\nd. Cac so nguyen to strobogrammatic mo rong < 1 trieu:")
for i in range(N):
    if la_strobo_mo_rong(i) and la_nguyen_to(i):
        print(i, end=" ")

print("\n\ne. Cac so khong strobo, khong nguyen to, nhung so xoay cua no la nguyen to:")
for i in range(N):
    x = xoay_so(i, False)

    if not la_strobo(i) and not la_nguyen_to(i) and x != -1 and la_nguyen_to(x):
        print(i, end=" ")