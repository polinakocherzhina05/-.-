from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
def preprocess_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]
    return ' '.join(tokens)
texts = []
file_names = ["c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", "c:\\Users\\User\\Desktop\\лингвистика python\\Легенда.txt", "c:\\Users\\User\\Desktop\\лингвистика python\\капитанская дочка1.txt"]
for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        text = preprocess_text(text)
        texts.append(text)
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(texts)
feature_names = tfidf.get_feature_names_out()
for i, text in enumerate(texts):
    print(f"Текст {i+1}:")
    feature_index = tfidf_matrix[i,:].nonzero()[1]
    tfidf_scores = zip(feature_index, [tfidf_matrix[i, x] for x in feature_index])
    sorted_tfidf_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)
    for word_index, score in sorted_tfidf_scores[:5]:
        print(f"- {feature_names[word_index]}: {score}")
plt.figure(figsize=(12, 6))
scores = [score for _, score in sorted_tfidf_scores[:10]]
words = [feature_names[word_index] for word_index, _ in sorted_tfidf_scores[:10]]
plt.bar(words, scores)
plt.xlabel('Слово')
plt.ylabel('TF-IDF Score')
plt.title('Топ-10 ключевых слов для первого текста')
plt.xticks(rotation=45)
plt.show()