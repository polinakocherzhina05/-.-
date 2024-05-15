with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
    text = file.read()
n = ''.join([char for char in text if char.isalpha() or char.isspace()])
print(n)