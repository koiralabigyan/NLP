import fasttext

# Small labelled dataset
training_data = [
"__label__positive The flight service is excellent",
"__label__positive The airline staff were very helpful",
"__label__positive Travel arrangements were smooth and comfortable",
"__label__positive The airport experience was pleasant",
"__label__positive Flights were on time and well managed",
"__label__negative The flight was delayed for hours",
"__label__negative Customer service was very poor",
"__label__negative The airport was overcrowded",
"__label__negative The travel experience was frustrating",
"__label__negative I had a terrible flight experience"
]

# Write dataset to temporary training file
with open("train_fasttext.txt", "w") as f:
    for line in training_data:
        f.write(line + "\n")

# Train FastText model
model = fasttext.train_supervised(
    input="train_fasttext.txt",
    epoch=50,
    lr=1.0,
    wordNgrams=2
)

# Test sentences
test_sentences = [
"The flight service was very good",
"The airline experience was terrible",
"Passengers had a smooth journey",
"The airport service was disappointing"
]

print("\n--- SENTIMENT PREDICTIONS ---\n")

for sentence in test_sentences:
    label, score = model.predict(sentence)

    print("Sentence:", sentence)
    print("Predicted Label:", label[0])
    print("Confidence:", round(score[0],3))
    print()

# Evaluate model
result = model.test("train_fasttext.txt")

print("\n--- MODEL EVALUATION ---")
print("Number of samples:", result[0])
print("Precision:", result[1])
print("Recall:", result[2])