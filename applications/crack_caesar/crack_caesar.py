# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

"""
| Letter | Percentage |
|:------:|-----------:|
|   E    |    11.53   |
|   T    |     9.75   |
|   A    |     8.46   |
|   O    |     8.08   |
|   H    |     7.71   |
|   N    |     6.73   |
|   R    |     6.29   |
|   I    |     5.84   |
|   S    |     5.56   |
|   D    |     4.74   |
|   L    |     3.92   |
|   W    |     3.08   |
|   U    |     2.59   |
|   G    |     2.48   |
|   F    |     2.42   |
|   B    |     2.19   |
|   M    |     2.18   |
|   Y    |     2.02   |
|   C    |     1.58   |
|   P    |     1.08   |
|   K    |     0.84   |
|   V    |     0.59   |
|   Q    |     0.17   |
|   J    |     0.07   |
|   X    |     0.07   |
|   Z    |     0.03   |
"""

import string 
# Your code here
def decode_cipher(input_file: str):
    known_frequency = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L", "W", "U", "G", "F", "B", "M", "Y", 
    "C", "P", "K", "V", "Q", "J", "X", "Z"]
    # creating string constant
    result = string.ascii_uppercase #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    # creating hash tables
    counted_cache = {} #key= char, value=times it is in the text
    letter_percentages_cache = {} #key=char, value  = %
    cipher_map_cache = {}
    #opening, reading and assigning the file to a variable
    with open(input_file) as f:
        cipher_text = f.read()
    
    #populating counted_cache
    for char in cipher_text:
        if char in result:
            if counted_cache.__contains__(char):
                counted_cache[char] += 1
            else:
                counted_cache[char] = 1
    #populating letter_percentage_cache  
    for letter in result:
        percentage = (counted_cache[letter] / len(cipher_text)) * 100
        letter_percentages_cache[letter] = percentage

    items = list(letter_percentages_cache.items())
    # sort in reverse
    items.sort(key = lambda x: -x[1])
    index = 0

    for (key, value) in items:
        cipher_map_cache[key] = known_frequency[index]
        index += 1
    decoded = ""
    
    for char in cipher_text:
        if char in result:
            char = cipher_map_cache[char]
        decoded += char
    return decoded

print(decode_cipher("applications/crack_caesar/ciphertext.txt"))