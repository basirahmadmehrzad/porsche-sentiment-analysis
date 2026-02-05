#!/usr/bin/env python3
import sys
import json
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)


def load_comments(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [record.get('comment', '') for record in data]


def preprocess(text, stopwords_set):
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = [word for word in text.split() if word not in stopwords_set]
    return " ".join(tokens)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)

    input_json = sys.argv[1]
    output_image = sys.argv[2] if len(sys.argv) > 2 else 'wordcloud.png'

    STOPWORDS = set(stopwords.words('english'))

    comments = load_comments(input_json)
    cleaned_text = ' '.join(preprocess(c, STOPWORDS) for c in comments)

    wc = WordCloud(width=800, height=400, background_color='white', stopwords=STOPWORDS, collocations=False)
    wc.generate(cleaned_text)
    wc.to_file(output_image)
    print(output_image)

    plt.figure(figsize=(12,6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()
