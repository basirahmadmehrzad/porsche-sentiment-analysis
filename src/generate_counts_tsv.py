# generate_counts_tsv.py
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv('cleaned_posts.txt', sep='\t', names=['post_id', 'text'], dtype=str)
analyzer = SentimentIntensityAnalyzer()
df['sentiment'] = df['text'].apply(lambda t: analyzer.polarity_scores(t)['compound'])

bins = [-1.0, -0.05, 0.05, 1.0]
labels = ['Negative', 'Neutral', 'Positive']
df['category'] = pd.cut(df['sentiment'], bins=bins, labels=labels)
counts = df['category'].value_counts().reindex(labels)

# ✅ Export to counts.tsv
counts.to_csv('counts.tsv', sep='\t', header=False)
print("✅ counts.tsv file generated.")
