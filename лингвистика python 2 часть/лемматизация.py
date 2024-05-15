import string
import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

nltk.download('stopwords')

stop_words = set(stopwords.words('russian'))

with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
    text = file.read()

def preprocess_text(text):

    text = ''.join([char for char in text if char not in string.punctuation])
    
    words = text.lower().split()
    
    words = [word for word in words if word not in stop_words]
    
    return words

processed_text = preprocess_text(text)


word_counts = Counter(processed_text)

def plot_word_frequency(word_freq, n):
    most_common_words = word_freq.most_common(n)
    words, counts = zip(*most_common_words)

    plt.figure(figsize=(12, 6))
    plt.bar(words, counts, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {n} Most Common Words')
    plt.xticks(rotation=45)
    plt.show()

plot_word_frequency(word_counts, 5)