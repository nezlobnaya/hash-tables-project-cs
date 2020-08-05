words = ["apple", "book", "cat", "dog", "egypt", "france"]

def my_hash(s, limit):
    string_utf = s.encode()

    total = 0
    for char in string_utf:
        total += char
        total &= 0xffffffff #limit total to 32 bits
    return total % limit

hash_table = [None] * 8

index =my_hash('hello', len(hash_table))
hash_table[index] = 'Value for hello'

index = my_hash('world', len(hash_table))
hash_table[index] = 'Value for world'

print(my_hash('hello', len(hash_table)))
print(hash_table[index])
print(hash_table)
