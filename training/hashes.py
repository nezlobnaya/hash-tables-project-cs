hash_table = [None] * 8

words = ["apple", "book", "cat", "dog", "egypt", "france"]

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def my_hash(s):
    string_utf = s.encode()

    total = 0
    for char in string_utf:
        total += char
        total &= 0xffffffff #limit total to 32 bits
    return total 

def hash_index(key):
    hash_num = my_hash(key)
    return hash_num % len(hash_table)

def put(key, val):
    index = hash_index(key)
    if hash_table[index] !=None:
        print(f"Collision! Overwriting {repr(hash_table[index])}!")
    hash_table[index] = val

def get(key):
    index = hash_index(key)
    return hash_table[index]



# index = my_hash('hello', len(hash_table))
# hash_table[index] = 'Value for hello'

# index = my_hash('world', len(hash_table))
# hash_table[index] = 'Value for world'

# print(my_hash('hello', len(hash_table)))
# print(hash_table[index])
# print(hash_table)
