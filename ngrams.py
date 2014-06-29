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
for n in range(1,23):
    output = {}
    for i in range(len(input)-n+1):
        g = ' '.join(input[i:i+n])
        output.setdefault(g, 0)
        output[g] += 1
    sorted_output = list(reversed(sorted(output.iteritems(), key=operator.itemgetter(1))))
    # save entries to file
    w = csv.writer(open("ngrams/ngrams"+str(n).zfill(2)+".csv", "w"))
    j=0
    while j<len(sorted_output) and sorted_output[j][1]>max(3,0.001*sorted_output[0][1]):
        w.writerow([sorted_output[j][1], sorted_output[j][0]])
        j=j+1
