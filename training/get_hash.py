class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]
  
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100
    
    # def add(self, key, val):
    #     h = self.get_hash(key)
    #     self.arr[h] = val
    
    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]
    
    # def delete(self, key):
    #     h = self.get_hash(key)
    #     self.arr[h] = None

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()

t.get_hash('vlad')
t.get_hash('vasya')
t.get_hash('vova')

t['march6'] = 130
print(t['march6'])
del t['march6']

print(t.arr)