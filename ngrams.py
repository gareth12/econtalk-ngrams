import operator
import os
import string
import csv

cumulative = ""

for file in os.listdir("./transcripts/"):
    if file.endswith(".txt"):
        with open ("./transcripts/" + file, "r") as f:
            i=f.read().replace('\n', '')
            cumulative = cumulative + i

input = cumulative.lower().translate(string.maketrans("",""), string.punctuation).split()

# compute ngrams for each n
for n in range(1,26):
    output = {}
    for i in range(len(input)-n+1):
        g = ' '.join(input[i:i+n])
        output.setdefault(g, 0)
        output[g] += 1
    sorted_output = list(reversed(sorted(output.iteritems(), key=operator.itemgetter(1))))
    # save top 1000 entries to a file
    entries = min(1000,len(sorted_output))
    w = csv.writer(open("ngrams/ngrams"+str(n)+".csv", "w"))
    for j in sorted_output[0:entries]:
        w.writerow([j[1], j[0]])
