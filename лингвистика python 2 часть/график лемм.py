import matplotlib.pyplot as plt
from collections import Counter
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
    text = file.read()

words = text.split()
lemmatized_words = [morph.parse(word)[0].normal_form for word in words]

word_counts = Counter(lemmatized_words)
top_words = word_counts.most_common(10)  
words, counts = zip(*top_words)

plt.bar(words, counts)
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.title('Наиболее частотные слова')
plt.xticks(rotation=45)
plt.show()