with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", "r", encoding="utf-8") as file:
    c = file.read()
    tokens = c.split(" ")
    print(tokens)