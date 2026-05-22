import math

# Cách 1: đếm số ước
so_nguyen_to_1 = lambda n: n > 1 and \
    sum(1 for i in range(1, n + 1) if n % i == 0) == 2

print("Cach 1:")
for i in range(1, 1000001):
    if so_nguyen_to_1(i):
        print(i, end=" ")


# Cách 2: tổng các ước = n + 1
so_nguyen_to_2 = lambda n: n > 1 and \
    sum(i for i in range(1, n + 1) if n % i == 0) == n + 1

print("\n\nCach 2:")
for i in range(1, 1000001):
    if so_nguyen_to_2(i):
        print(i, end=" ")


# Cách 3: dùng any + căn bậc hai
so_nguyen_to_3 = lambda n: n > 1 and \
    not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))

print("\n\nCach 3:")
for i in range(1, 1000001):
    if so_nguyen_to_3(i):
        print(i, end=" ")


# Cách 4: dùng filter + lambda trong hàm def
def F(k):
    return k > 1 and len(
        list(filter(lambda x: k % x == 0, range(1, k + 1)))
    ) == 2


print("\n\nCach 4:")
for i in range(1, 1000001):
    if F(i):
        print(i, end=" ")