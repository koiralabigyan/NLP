import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")

# Dataset text (source: english.onlinekhabar.com)
text = """Doha-Kathmandu flights to operate despite growing Middle East tensions.
Amid rising tensions in the Middle East that have disrupted international air travel, flights between Doha and Kathmandu are set to continue operating.

According to the schedule released by Qatar’s national carrier Qatar Airways, flights from Doha to Kathmandu will operate on March 16 and 17. Likewise, flights from Kathmandu to Doha are scheduled for March 17 and 18.

Passengers travelling from Nepal to Qatar or those transiting through Doha to other international destinations will be able to use these flights.

Along with Kathmandu, Qatar Airways is also operating special flights to several Asian and international destinations, including New Delhi, Mumbai, Dhaka, Bangkok, Istanbul, London, and Paris.

As tensions escalate in the Middle East, several countries have taken precautionary measures in their airspace, leading to the cancellation or rerouting of some flights."""

# Process text
doc = nlp(text)
print("\n--- DEPENDENCY RELATIONS ---")

# Print token, dependency, and head word
for token in doc:
    print(f"{token.text:<15} {token.dep_:<12} {token.head.text}")

# Select 1 sentence for visualization
sentence = list(doc.sents)[0]

# Visualize dependency tree
displacy.serve(sentence, style="dep", auto_select_port=True)