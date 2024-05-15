import spacy

nlp = spacy.load("ru_core_news_sm")

def extract_named_entities(text):
    doc = nlp(text)
    named_entities = []

    for entity in doc.ents:
        named_entities.append((entity.text, entity.label_))

    return named_entities

with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
    text = file.read()

named_entities = extract_named_entities(text)
print(named_entities)