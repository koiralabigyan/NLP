import spacy

text = "Contact us at info@example.com or call +977-9812345678. The meeting is scheduled on 12/08/2024."

# Load spaCy Model
nlp = spacy.load("en_core_web_sm")

# Tokenization using spaCy
doc = nlp(text)
tokens = [token.text for token in doc]

print("\nspaCy Tokens:")
print(tokens)

# Extra Linguistic Info
print("\nToken Details:")
print(f"{'Text':<20} {'Lemma':<20} {'POS':<10}")
print("-" * 50)

for token in doc:
    print(f"{token.text:<20} {token.lemma_:<20} {token.pos_:<10}")
