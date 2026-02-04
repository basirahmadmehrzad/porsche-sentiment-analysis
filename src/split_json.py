#!/usr/bin/env python3

"""
split_json.py

This script converts a JSON file containing a list of Reddit posts
into a line-by-line JSON format (one JSON object per line).

This format is easier to process using Hadoop streaming and
Python-based text processing pipelines.
"""

import json
import sys


def split_json(input_file):
    """
    Reads a JSON array file and prints each object
    as a separate JSON line to stdout.
    """
    with open(input_file, "r", encoding="utf-8") as f:
        posts = json.load(f)

    for post in posts:
        print(json.dumps(post, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split_json.py <input_json_file>", file=sys.stderr)
        sys.exit(1)

    input_json = sys.argv[1]
    split_json(input_json)
