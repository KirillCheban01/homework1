
VOWELS = "a, e, i, o, u"
word = input("Введите слово:")
count = 0
for char in word:
    if char in VOWELS:
        count += 1
print(count)