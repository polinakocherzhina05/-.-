import spacy
nlp = spacy.load("en_core_web_sm")
with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
    text = file.read()
doc = nlp(text)
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)