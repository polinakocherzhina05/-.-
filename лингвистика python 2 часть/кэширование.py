import pymorphy2

morph = pymorphy2.MorphAnalyzer()
lemma_cache = {}

def lemmatize_word(word):
    if word in lemma_cache:
        return lemma_cache[word]
    else:
        parsed_word = morph.parse(word)[0]
        lemma = parsed_word.normal_form
        lemma_cache[word] = lemma
        return lemma

with open('c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()

for word in words:
    lemma = lemmatize_word(word)
    print(f'Слово: {word}, Лемма: {lemma}')