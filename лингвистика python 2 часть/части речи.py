import pymorphy2
import matplotlib.pyplot as plt
morph = pymorphy2.MorphAnalyzer()
with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
     text = file.read()
words = text.split()
pos_list = []
for word in words:
    parsed_word = morph.parse(word)[0]  
    pos = parsed_word.tag.POS
    if pos is not None:
        pos_list.append(pos)
pos_freq = {pos: pos_list.count(pos) for pos in set(pos_list)}
plt.figure(figsize=(10, 6))
plt.bar(pos_freq.keys(), pos_freq.values(), color='skyblue')
plt.xlabel('Часть речи')
plt.ylabel('Частотность')
plt.title('Распределение частотности частей речи в тексте')
plt.show()