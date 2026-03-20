import re
text = "Contact us at info@example.com or call +9779812345678. The meeting is scheduled on 12/08/2024."

# Basic Cleaning

text = text.lower() # Change to lower case
text = re.sub(r"[^\w\s]", "", text) # Remove punctuation (keep only words and spaces)
text = re.sub(r"\s+", " ", text) # Remove extra spaces

print("Cleaned Text:", text)