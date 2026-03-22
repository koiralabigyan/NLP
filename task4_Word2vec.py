import spacy
from gensim.models import Word2Vec
nlp = spacy.load("en_core_web_sm")

# Dataset text (source: english.onlinekhabar.com)
text = """Doha-Kathmandu flights to operate despite growing Middle East tensions.
Amid rising tensions in the Middle East that have disrupted international air travel, flights between Doha and Kathmandu are set to continue operating.

According to the schedule released by Qatar’s national carrier Qatar Airways, flights from Doha to Kathmandu will operate on March 16 and 17. Likewise, flights from Kathmandu to Doha are scheduled for March 17 and 18.

Passengers travelling from Nepal to Qatar or those transiting through Doha to other international destinations will be able to use these flights.

Along with Kathmandu, Qatar Airways is also operating special flights to several Asian and international destinations, including New Delhi, Mumbai, Dhaka, Bangkok, Istanbul, London, and Paris."""

doc = nlp(text)
# Tokenize sentences
sentences = []
for sent in doc.sents:
    tokens = [token.text.lower() for token in sent if token.is_alpha]
    sentences.append(tokens)

print("\nTokenized Sentences:")
print(sentences)

# Train Word2Vec model
model = Word2Vec(
    sentences,
    vector_size=100,
    window=5,
    min_count=1,
    workers=4
)

# Target words from the article
target_words = ["flights", "doha", "operate", "travel", "passengers"]

print("\n--- MOST SIMILAR WORDS ---")

for word in target_words:
    if word in model.wv:
        print(f"\nTop similar words for '{word}':")
        similar_words = model.wv.most_similar(word, topn=5)

        for sim_word, score in similar_words:
            print(f"{sim_word} : {score:.3f}")