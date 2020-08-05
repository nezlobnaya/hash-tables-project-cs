class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        # Initialize hash table
        self.capacity = capacity
        self.size = 0 
        self.buckets = [None] * self.capacity 

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.buckets)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.capacity

    """
    ********************************************
    # Generate a hash for a given key
	# Input:  key - string
	# Output: Index from 0 to self.capacity

    """
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        h = 0xcbf29ce484222325
        key_utf8 = key.encode()
        for char in key_utf8:
            h *= 0x100000001b3
            h &= 0xffffffffffffffff
            h ^= char
        return h

        # fnv_prime = 1099511628211
        # offset_basis =  14695981039346656037
        # hash_value = offset_basis
        # key_utf8 = key.encode()
        # for byte in key_utf8:
        #     hash_value = hash_value ^ byte
        #     hash_value = hash_value * fnv_prime
        # return hash_value

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for char in key:
            hash = (hash * 33) + ord(char)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # Perform modulus to keep the index in range [0, self.capacity - 1]
        # return self.djb2(key) % self.capacity
        return self.fnv1(key) % self.capacity
    """
    ********************************************
    """

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # 1. Increment size
        self.size += 1
        # 2. Compute index of key
        index = self.hash_index(key)
        # Go to the node corresponding to the hash index
        node = self.buckets[index]
        # 3. If bucket is empty:
        if node is None:
            # Create node, add it, return
            self.buckets[index] = HashTableEntry(key, value)
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)
            return
        #hash collisions handled with Linked List Chaining.
        elif node.key is key:
            node.value = value
        # 4. Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:
            prev = node
            node = node.next
            # Add a new node at the end of the list with provided key/value
        prev.next = HashTableEntry(key, value)
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # 1. Compute hash
        index = self.hash_index(key)
        node = self.buckets[index]
        prev = None
        # 2. Iterate to the requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # Now, node is either the requested node or none
        if node is None:
            print("Key is not found!")
            return None
        else:
            self.size -= 1
            result = node.value
            # Delete this element in linked list
            if prev is None:
                self.buckets[index] = node.next # May be None, or the next match
            else:
                prev.next = prev.next.next # LinkedList delete by skipping over
            return result


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # 1. Compute hash index
        index = self.hash_index(key)
        # 2. Go to first node in list at bucket
        node = self.buckets[index]
        # 3. Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        # 4. Now, node is the requested key/value pair or None
        if node is None:
            return None
        else:
            return node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_ht = HashTable(new_capacity)
        for entry in self.buckets:
            if entry:
                new_ht.put(entry.key, entry.value)
                if entry.next:
                    current = entry
                    while current.next:
                        current = current.next
                        new_ht.put(current.key, current.value)
        self.buckets = new_ht.buckets
        self.capacity = new_ht.capacity


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
