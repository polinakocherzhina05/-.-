from gensim.models import KeyedVectors

# Загрузка предобученной модели fastText
model_path = 'c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt'
model = KeyedVectors.load(model_path)

# Пример использования модели
similar_words = model.most_similar('king')
print(similar_words)