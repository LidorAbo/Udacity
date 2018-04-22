"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000
        self.size = 100

    def store(self, string):
        index = self.calculate_hash_value(string)
        self.table[index] = string

    def lookup(self, string):
        index = self.calculate_hash_value(string)
        if self.table[index] is not None:
            return index
        return -1

    def calculate_hash_value(self, string):
        hash_value = (ord(string[0]) * self.size) + ord(string[1])
        if hash_value <= 10000:
            return hash_value
        return -1


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))