class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]
  
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100
    
    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
    
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def delete(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()

print(t.get_hash('vlad'))
print(t.get_hash('vasya'))
print(t.get_hash('vova'))