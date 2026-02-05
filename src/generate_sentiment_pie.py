#!/usr/bin/env python3
import sys, csv
import matplotlib.pyplot as plt

# usage: python3 generate_sentiment_pie.py counts.tsv pie.png

counts_file = sys.argv[1]
out_png     = sys.argv[2]

labels = []
sizes  = []

with open(counts_file) as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if len(row) == 2:
            labels.append(row[0])
            sizes .append(int(row[1]))

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
ax.axis("equal")
plt.savefig(out_png)
