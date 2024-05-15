import pymorphy2

def process_text(text):
    morph = pymorphy2.MorphAnalyzer()

    words = text.split()
    processed_words = []
    
    for word in words:
        parsed_word = morph.parse(word)[0]
        
        if parsed_word.tag.POS in {'NOUN', 'ADJF'}:
            inflected_word = parsed_word.inflect({'ablt'})
        elif parsed_word.tag.POS == 'VERB':
            inflected_word = parsed_word.inflect({'past', 'femn'})
        else:
            inflected_word = None
        
        if inflected_word:
            processed_word = inflected_word.word
        else:
            processed_word = word
        
        processed_words.append(processed_word)

    processed_text = ' '.join(processed_words)
    return processed_text

# Пример использования
with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
    text = file.read()

processed_text = process_text(text)
print(processed_text)

modified_text = processed_text.replace("лекарство", "гроза")
print(modified_text)