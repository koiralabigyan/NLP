import re
import string
import emoji
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

reviews = [
"I love this phone!!! [SMILING_FACE] Battery life is amazing.",
"Worst delivery ever [ANGRY_FACE] waited 5 days!!!",
"Camera quality is decent [THUMBS_UP] but price is high.",
"Totally worth it [HAPPY_FACE] will recommend to friends.",
"Not happy [SAD_FACE] screen cracked in 2 weeks.",
"Excellent sound quality [SMILING_FACE] with long battery life.",
"Poor customer support [ANGRY_FACE], never buying again.",
"Fast delivery [THUMBS_UP] and good packaging.",
"Product stopped working in a week [SAD_FACE].",
"Amazing features [HAPPY_FACE], totally satisfied.",
"Battery drains quickly [ANGRY_FACE], disappointed.",
"Stylish design [SMILING_FACE], looks premium.",
"Late delivery [SAD_FACE], had to wait 1 week.",
"Excellent camera [HAPPY_FACE], clear pictures.",
"Screen scratched easily [ANGRY_FACE], not happy.",
"Love the lightweight design [SMILING_FACE].",
"Price is too high [SAD_FACE], not worth it.",
"Super fast processing [HAPPY_FACE], very smooth.",
"The sound is too low [ANGRY_FACE], disappointed.",
"Highly recommend [SMILING_FACE], very useful.",
"Package damaged [SAD_FACE], poor handling.",
"Good value for money [HAPPY_FACE], satisfied.",
"The device heats up quickly [ANGRY_FACE].",
"Impressive battery life [SMILING_FACE], lasts long.",
"Customer service was rude [ANGRY_FACE].",
"Compact and portable [HAPPY_FACE], love it.",
"Screen quality is poor [SAD_FACE].",
"Fast setup [SMILING_FACE], works perfectly.",
"Not durable [ANGRY_FACE], broke after few uses.",
"Highly functional [HAPPY_FACE], works as expected.",
"Missing accessories [SAD_FACE], incomplete package.",
"Great for daily use [SMILING_FACE], very handy.",
"Stopped working suddenly [ANGRY_FACE], disappointed.",
"Lightweight [HAPPY_FACE] and easy to carry.",
"Battery issue [SAD_FACE], needs frequent charging.",
"Amazing display [SMILING_FACE], vivid colors.",
"Overpriced [ANGRY_FACE], not satisfied.",
"Very fast [HAPPY_FACE] and reliable.",
"Delivery was delayed [SAD_FACE], unhappy.",
"Easy to use [SMILING_FACE], very intuitive.",
"Not recommended [ANGRY_FACE], poor quality.",
"Excellent support [HAPPY_FACE], resolved issues quickly.",
"Screen cracked [SAD_FACE], fragile product.",
"Very comfortable [SMILING_FACE] to wear.",
"Product malfunctioned [ANGRY_FACE], returned it.",
"Good performance [HAPPY_FACE], very happy.",
"Lost package [SAD_FACE], customer service bad.",
"Sleek design [SMILING_FACE], highly satisfied.",
"Stopped charging [ANGRY_FACE], broken unit.",
"Top-notch quality [HAPPY_FACE], worth every penny.",
"Bad build [SAD_FACE], not recommended."
]

# Map tags to emoji aliases
emoji_alias_map = {
    "[SMILING_FACE]": ":smiling_face_with_smiling_eyes:",
    "[ANGRY_FACE]": ":angry_face:",
    "[THUMBS_UP]": ":thumbs_up:",
    "[HAPPY_FACE]": ":grinning_face_with_big_eyes:",
    "[SAD_FACE]": ":crying_face:"
}

def convert_emojis(text):
    for tag, alias in emoji_alias_map.items():
        text = text.replace(tag, alias)
    return emoji.emojize(text, language='alias')

def clean_text(text):
    text = convert_emojis(text)
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Tokenize & Remove Stopwords
stop_words = set(stopwords.words('english'))

def tokenize_remove_stopwords(text):
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

# Full Processing
cleaned_reviews = [clean_text(review) for review in reviews]
final_processed = [tokenize_remove_stopwords(review) for review in cleaned_reviews]

# Print
for review in final_processed:
    print(review)