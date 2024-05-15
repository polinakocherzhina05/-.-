from collections import Counter

with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
    text = file.read()

words = text.lower().split()

words = [word.strip('.,!?()[]{}"\'') for word in words]

word_counter = Counter(words)

total_words = sum(word_counter.values())

print("Общее количество слов в тексте:", total_words)