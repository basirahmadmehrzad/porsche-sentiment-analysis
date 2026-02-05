import json
import csv

input_file = "/media/sf_big_data/youtube_comments_filtered.json"
output_file = "comments.csv"

with open(input_file, "r") as infile:
    data = json.load(infile)  # not json.loads(line)

with open(output_file, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["video_id", "author", "comment"])

    for obj in data:
        writer.writerow([obj.get("video_id", ""), obj.get("author", ""), obj.get("comment", "")])
