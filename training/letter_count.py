# Given a string, can we figure out how many times each letter appears in it? 

def letter_count(s):
    # Dict where keys are letters and values will be an incrementing counter
    d = {}
    for char in s:
        if char.isspace():
            continue

        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    
    return d

def double_letter(s):
    # store letters as keys and a counter as value
    # Find all letters,(or just the one letter) where value > 1
        # Dict where keys are letters and values will be an incrementing counter
    d = set()
    for char in s:
        if char.isspace():
            continue

        if char not in d:
            d.add(char)
        else:
            return char



print(double_letter("abecdef")) # should be e

# print(letter_count("aaabbc"))
# print(letter_count("Hello!"))
# print(letter_count("The quick brown fox jumps over the lazy dogs"))