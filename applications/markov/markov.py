import random

with open("applications/markov/input.txt") as f:
    words = f.read()

# Your code here
lookup_table = {}
def analyze_text(words):
    words = words.split()
    for i in range(len(words) - 1):
        word = words[i]
        if word not in lookup_table:
            lookup_table[word] = [words[i + 1]]
        else:
            lookup_table[word].append(words[i + 1])
    return lookup_table

def construct_text(lookup_table):
    # start_words are random keys that are capitalized 
    start_words = [key for key in lookup_table.keys() if key[0].isupper() or (key[0] == '"' and key[1].isupper())]
    start_word = random.choice(start_words)
    print(start_word, end=" ")
    punctuation = '''.?!"'''
    stop_words = []
    middle_words = []
    for arr in lookup_table.values():
        for value in arr:
            if value[-1] in punctuation:
                stop_words.append(value)
            elif value[0] != '"':
                middle_words.append(value)
    for i in range(random.randint(0, 50)):
        print(random.choice(middle_words), end=" ")
    rand_stop_word = random.choice(stop_words)
    print(rand_stop_word)


analyze_text(words)


# TODO: construct 5 random sentences
# Your code here
print("Sentence 1")
construct_text(lookup_table)
print("Sentence 2")
construct_text(lookup_table)
print("Sentence 3")
construct_text(lookup_table)
print("Sentence 4")
construct_text(lookup_table)
print("Sentence 5")
construct_text(lookup_table)
