import math

# i) Số palindrome
so_palindrome = lambda n: str(n) == str(n)[::-1]

print("i) So palindrome:")
for i in range(1, 1000001):
    if so_palindrome(i):
        print(i, end=" ")


# j) Số nguyên tố palindrome
so_nguyen_to_palindrome = lambda n: \
    n > 1 and \
    str(n) == str(n)[::-1] and \
    not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))

print("\n\nj) So nguyen to palindrome:")
for i in range(1, 1000001):
    if so_nguyen_to_palindrome(i):
        print(i, end=" ")