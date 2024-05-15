import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import math

# Загрузка стоп-слов
nltk.download('stopwords')

# Открытие файлов
with open(r'c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt', encoding='utf-8') as doc_1, open(r'c:\\Users\\User\\Desktop\\лингвистика python\\Легенда.txt', encoding='utf-8') as doc_2:
    line1 = doc_1.read()
    line2 = doc_2.read()

# Токенизация и удаление стоп-слов
tokenizer = RegexpTokenizer(r'\w+')
stop_words = set(stopwords.words('english'))

tokens_1 = tokenizer.tokenize(line1.lower())
tokens_2 = tokenizer.tokenize(line2.lower())

text_with_no_stopwords_1 = [word for word in tokens_1 if word not in stop_words]
text_with_no_stopwords_2 = [word for word in tokens_2 if word not in stop_words]

bag_of_words_1 = set(text_with_no_stopwords_1)
bag_of_words_2 = set(text_with_no_stopwords_2)

# Создание словарей с нулевыми значениями
dict_1 = dict.fromkeys(bag_of_words_1, 0)
dict_2 = dict.fromkeys(bag_of_words_2, 0)

# Подсчет частоты слов в каждом документе
for word in text_with_no_stopwords_1:
    dict_1[word] += 1

for word in text_with_no_stopwords_2:
    dict_2[word] += 1

# Функция вычисления TF (term frequency)
def compute_term_frequency(word_dictionary, bag_of_words):
    term_frequency_dictionary = {}
    length_of_bag_of_words = len(bag_of_words)

    for word, count in word_dictionary.items():
        term_frequency_dictionary[word] = count / float(length_of_bag_of_words)

    return term_frequency_dictionary

# Функция вычисления IDF (inverse document frequency)
def compute_inverse_document_frequency(full_doc_list):
    idf_dict = {}
    length_of_doc_list = len(full_doc_list)

    # Подсчет, в скольких документах встречается каждое слово
    for doc in full_doc_list:
        for word, value in doc.items():
            if value > 0:
                idf_dict[word] = idf_dict.get(word, 0) + 1

    # Вычисление IDF
    for word, value in idf_dict.items():
        idf_dict[word] = math.log(length_of_doc_list / float(value))

    return idf_dict

final_idf_dict = compute_inverse_document_frequency([dict_1, dict_2])

print("TF для документа 1:", compute_term_frequency(dict_1, text_with_no_stopwords_1))
print("TF для документа 2:", compute_term_frequency(dict_2, text_with_no_stopwords_2))
print("IDF для обоих документов:", final_idf_dict)

for word in bag_of_words_2:
    dict_2[word] = 1

print(dict_1, dict_2)

def compute_term_frequency(word_dictionary, bag_of_words):
    term_frequency_dictionary = {}
    length_of_bag_of_words = len(bag_of_words)

    for word, count in word_dictionary.items():
        term_frequency_dictionary[word] = count / float(length_of_bag_of_words)

    return term_frequency_dictionary

print(compute_term_frequency(dict_1, bag_of_words_1), (dict_2, bag_of_words_2))

import math

def compute_inverse_document_frequency(full_doc_list):
    idf_dict = {}
    length_of_doc_list = len(full_doc_list)

    idf_dict = dict.fromkeys(full_doc_list[0].keys(), 0)
    for word, value in idf_dict.items():
        idf_dict[word] = math.log(length_of_doc_list / (float(value)+1))

    return idf_dict

final_idf_dict = compute_inverse_document_frequency([dict_1])
#print(final_idf_dict)