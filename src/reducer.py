#!/usr/bin/env python3
import sys

last_id = None
for line in sys.stdin:
    post_id, cleaned_text = line.rstrip('\n').split('\t', 1)
    if post_id != last_id:
        print(f"{post_id}\t{cleaned_text}")
        last_id = post_id
