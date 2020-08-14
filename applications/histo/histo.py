# Your code here
with open("applications/histo/robin.txt") as f:
    s = f.read()

import re #import regex module
def hist(s):
    counts = {}
    s = s.lower()
    # get rid of punctuation
    s = re.sub(r'[^\w\s]','', s) #regular expression replacement with re.sub
    # iterate through each word in the sentence using split
    for word in s.split():
        # if it's the first time seeing the key
        if word not in counts:
            # set the value to 1
            counts[word] = 1
        # if it's a duplicate key
        else:
            # add 1 to the value
            counts[word] += 1
    # sort dictionary
    list_of_items = list(counts.items())
    list_of_items.sort(key = lambda x: -x[1])
    # iterate through each tuple in the list to construct histogram
    for word, count in list_of_items:
        print(f"{word:<15} {count * '#'}")

hist(s)
