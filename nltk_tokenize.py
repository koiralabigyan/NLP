from nltk.tokenize import word_tokenize

text = "Contact us at test@example.com or call +977-98123451234. The meeting is scheduled on 12/02/2026."

tokens = word_tokenize(text)
print(tokens)