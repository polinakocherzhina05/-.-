from pymystem3 import Mystem

mystem = Mystem()
with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
    text = file.read()

lemmas = mystem.lemmatize(text)
analysis = mystem.analyze(text)

print(lemmas)
print(analysis)
