#Processes line-based Reddit JSON input, cleans comment text, and prepares it for distributed processing.


#!/usr/bin/env python3
import sys, json, re
from nltk.corpus import stopwords

# Patterns
URL_RE   = re.compile(r'https?://\S+')
EMOJI_RE = re.compile(
    "[" 
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    "]+", flags=re.UNICODE)

stops = set(stopwords.words('english'))

for line in sys.stdin:
    post = json.loads(line)
    text = (post.get('title','') + ' ' + post.get('selftext','')).lower()
    text = URL_RE.sub('', text)
    text = EMOJI_RE.sub('', text)
    tokens = re.findall(r'\b\w+\b', text)
    cleaned = [t for t in tokens if t not in stops]
    if cleaned:
        # emit: postID<TAB>cleaned_text
        print(f"{post['id']}\t{' '.join(cleaned)}")
