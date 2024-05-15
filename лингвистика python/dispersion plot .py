import nltk
import matplotlib.pyplot as plt
with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
    text = file.read()
tokens = nltk.word_tokenize(text)
text = nltk.Text(tokens)
words_to_plot = ['Мерцалов', 'доктор', 'время']
indexes = [index for index, word in enumerate(text) if word in words_to_plot]
for i, word in enumerate(words_to_plot):
    word_indexes = [idx for idx in indexes if text[idx] == word]
    plt.scatter(word_indexes, [i] * len(word_indexes), label=word)

plt.yticks(range(len(words_to_plot)), words_to_plot)
plt.xlabel('Распределение слов в тексте')
plt.title('Дисперсионный график')
plt.show()