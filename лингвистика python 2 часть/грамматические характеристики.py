import pymorphy2

morph = pymorphy2.MorphAnalyzer()

with open('c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt', 'r') as file:
    text = file.read()

words = text.split()

for word in words:
    parsed_word = morph.parse(word)[0]  
    print(f'Слово: {word}, Лемма: {parsed_word.normal_form}, Часть речи: {parsed_word.tag.POS}, Падеж: {parsed_word.tag.case}')