import matplotlib.pyplot as plt
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
    text = file.read()
tokens = word_tokenize(text.lower())
tokens = [word for word in tokens if word.isalpha()]

stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word not in stop_words and len(word) >= 3]

freq_dist = FreqDist(tokens)

plt.figure(figsize=(12, 6))
freq_dist.plot(20, cumulative=False)
plt.title('Top 20 частотных слов (длина >= 3)')
plt.xlabel('Слово')
plt.ylabel('Частота')
plt.show()