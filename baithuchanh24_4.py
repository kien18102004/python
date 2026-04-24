import math

# a) Trị tuyệt đối
a = lambda n: abs(n)

# b) n + 15
b = lambda n: n + 15

# c) Tích x, y
c = lambda x, y: x * y

# d) Bội của 13 hoặc 19
d = lambda n: n % 13 == 0 or n % 19 == 0

# e) Diện tích hình tròn
e = lambda r: math.pi * r * r

# f) Chu vi hình chữ nhật
f = lambda d, r: 2 * (d + r)

# g) Số chính phương
g = lambda n: int(math.sqrt(n))**2 == n

# h) Số nguyên tố
h = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

# i) Kiểm tra tam giác và loại tam giác
i = lambda a, b, c: (
    "Không phải tam giác" if (a + b <= c or a + c <= b or b + c <= a)
    else "Tam giác đều" if (a == b == c)
    else "Tam giác cân" if (a == b or b == c or a == c)
    else "Tam giác vuông" if (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a)
    else "Tam giác thường"
)

# Test thử
print(a(-5))
print(b(10))
print(c(3, 4))
print(d(26))
print(e(2))
print(f(5, 3))
print(g(16))
print(h(7))
print(i(3, 4, 5))