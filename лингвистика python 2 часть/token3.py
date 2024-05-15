import nltk
nltk.download('punkt')

with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", "r", encoding="utf-8") as file:
    a = file.read()
    tokens = nltk.word_tokenize(a)
    print(tokens)