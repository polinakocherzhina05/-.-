file = open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8")

words = 0

for line in file:
    words += len(line.split())

print("Words:", words)