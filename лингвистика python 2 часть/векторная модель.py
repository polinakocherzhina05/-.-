from gensim.models import Word2Vec

model = Word2Vec.load("c:\\Users\\User\\Desktop\\лингвистика python\\ruscorpora_upos_skipgram_300_5_2018.txt")

words = ["apple", "banana", "orange", "grape", "cherry"]

for word in words:
    similar_words = model.wv.most_similar(word, topn=10)
    print(f"10 ближайших соседей для слова '{word}':")
    for similar_word, similarity in similar_words:
        print(f"{similar_word}: {similarity}")

word1 = "apple"
word2 = "orange"

cosine_similarity = model.wv.similarity(word1, word2)
print(f"Косинусное сходство между '{word1}' и '{word2}': {cosine_similarity}")

result = model.wv.most_similar(positive=['pizza', 'Italy'], negative=['Siberia'])
print(f"Результат аналогии 'Italy - Siberia + pizza': {result}")

words = ["apple", "banana", "orange", "grape", "cherry"]

odd_word = model.doesnt_match(words)
print(f"Отличное слово в группе: {odd_word}")