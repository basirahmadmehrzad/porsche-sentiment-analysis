#!/usr/bin/env python3

"""
split_json.py

Converts a JSON array of Reddit posts into a line-based JSON file
(one JSON object per line).

Output file:
    posts_per_line.json

This format is required for Hadoop MapReduce and
large-scale text processing.
"""

import json


def split_json(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        posts = json.load(f)

    with open(output_file, "w", encoding="utf-8") as out:
        for post in posts:
            out.write(json.dumps(post, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    input_json = "porsche_reddit_posts.json"
    output_json = "posts_per_line.json"

    split_json(input_json, output_json)

    print(
        f"Converted '{input_json}' to line-based format "
        f"and saved as '{output_json}'."
    )
