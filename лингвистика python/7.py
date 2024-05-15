from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors

# Преобразование модели GloVe в формат Word2Vec
glove_input_file = 'c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt'
word2vec_output_file = 'c:\\Users\\User\\Desktop\\лингвистика python\\чд.txt'
glove2word2vec(glove_input_file, word2vec_output_file)

# Загрузка модели Word2Vec
model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)

# Пример использования модели
similar_words = model.most_similar('king')
print(similar_words)