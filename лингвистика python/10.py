import stanza

stanza.download(lang="ru", package=None, processors={"tokenize":""})

if __name__ == "__main__":
    with open("c:\\Users\\User\\Desktop\\лингвистика python\\Чудесный доктор.txt", encoding="utf-8") as file:
        text = file.read()

    ppln = stanza.Pipeline(
        lang='ru',
        processors='tokenize',
        tokenize_model_path=text,
        use_gpu=True
    )

    SOME_TEXT = "Your Russian text goes here"
    doc = ppln(SOME_TEXT)
    print(doc)