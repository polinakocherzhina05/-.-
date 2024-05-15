from pymystem3 import Mystem
import matplotlib.pyplot as plt

mystem = Mystem()

with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
    text = file.read()

lemmas = mystem.lemmatize(text)

# Выберите конкретную лемму, частотность которой вы хотите отобразить
target_lemma = "сердце"
lemma_counts = [lemmas[:i+1].count(target_lemma) for i in range(len(lemmas))]

plt.plot(range(len(lemmas)), lemma_counts)
plt.xlabel('Порядковый номер слова в тексте')
plt.ylabel('Частотность леммы "{}"'.format(target_lemma))
plt.title('Изменение частотности леммы "{}" в тексте'.format(target_lemma))
plt.show()