#!/usr/bin/env python3

import json
from datetime import datetime
import os
import praw

# Reddit API credentials


CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = "PorscheSentimentAnalysis/1.0"

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError(
        "Reddit API credentials not found. "
        "Please set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET as environment variables."
    )

# Project configuration (time selection)


SEARCH_QUERY = "porsche"
START_DATE = datetime(2025, 1, 1)
END_DATE = datetime.utcnow()
RESULT_LIMIT = None  # None = fetch as many as possible


# Initialize Reddit client


reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)


# Data collection


collected_posts = []

print(
    f"Collecting Reddit posts containing '{SEARCH_QUERY}' "
    f"from {START_DATE.date()} to {END_DATE.date()}..."
)

for submission in reddit.subreddit("all").search(
    SEARCH_QUERY, sort="new", limit=RESULT_LIMIT
):
    post_time = datetime.utcfromtimestamp(submission.created_utc)

    if post_time < START_DATE:
        break

    if START_DATE <= post_time <= END_DATE:
        collected_posts.append({
            "id": submission.id,
            "created_utc": submission.created_utc,
            "author": str(submission.author),
            "subreddit": str(submission.subreddit),
            "score": submission.score,
            "num_comments": submission.num_comments,
            "title": submission.title,
            "selftext": submission.selftext,
            "url": submission.url
        })


# Save output


output_file = "porsche_reddit_posts.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(collected_posts, f, ensure_ascii=False, indent=2)

print(
    f"Collection complete. "
    f"{len(collected_posts)} posts saved to '{output_file}'."
)
