s = input("Nhập chuỗi S: ")
word = input("Nhập từ cần đếm: ")

# chuẩn hoá về chữ thường để đếm cho chính xác
s = s.lower()
word = word.lower()

# tách thành từng từ
words = s.split()

count = 0
for w in words:
    if w.strip(".,") == word:
        count += 1

print(f"Số từ '{word}' là {count}")