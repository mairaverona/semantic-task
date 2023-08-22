import spacy

nlp = spacy.load("en_core_web_md")
word1 = nlp("pizza")
word2 = nlp("tomato")
word3 = nlp("person")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp("pizza tomato person")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
