import nltk
with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
    text = file.read()
tokens = nltk.word_tokenize(text)
text = nltk.Text(tokens)
word_to_check = 'он'
print('Слова с похожим контекстом на слово "{}":'.format(word_to_check))
text.similar(word_to_check)

print('\nОбщие контексты для слов "Мерцалов" и "доктор":')
concordance_list = text.concordance_list(word_to_check)
for entry in concordance_list:
    print(entry.line)
print('\nЧасто встречающиеся словосочетания (коллокации):')
text.collocations()