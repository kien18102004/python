# k) Số lộc phát

# Cách 1: dùng all
so_loc_phat_1 = lambda n: all(ch in '68' for ch in str(n))

print("Cach 1:")
for i in range(1, 1000001):
    if so_loc_phat_1(i):
        print(i, end=" ")


# Cách 2: đếm số 6 và 8
so_loc_phat_2 = lambda n: \
    str(n).count('6') + str(n).count('8') == len(str(n))

print("\n\nCach 2:")
for i in range(1, 1000001):
    if so_loc_phat_2(i):
        print(i, end=" ")


# l) Số lộc phát palindrome
so_loc_phat_palindrome = lambda n: \
    all(ch in '68' for ch in str(n)) and str(n) == str(n)[::-1]

print("\n\nSo loc phat palindrome:")
for i in range(1, 1000001):
    if so_loc_phat_palindrome(i):
        print(i, end=" ")