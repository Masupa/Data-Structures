"""
    ReadMe:
        - This is a basic implementation of the Hash Table. With this implementation, I have not factored in Collision
          resolution. The main goal of this implementation was to hash any given ints or str into a slot in the Hash
          Table

        - Note of hash function: Even though they are different ways to implement the function, my implementation
          only focuses on the basic Remainder Method implementation.
"""


class HashTable:

    def __init__(self, size):
        self._size = size
        self.table = [None] * self._size

    def get_table(self):
        return self.table

    def _hash_function(self, item):
        # Edge Cases - Item is either an Integer or a string
        if type(item) is int:
            return item % self._size
        else:
            ord_sum = 0
            for i in range(len(item)):
                ord_sum += ord(item[i])
            return ord_sum % self._size

    def insertion(self, item):
        hash_value = self._hash_function(item)
        self.table[hash_value] = item

    def __str__(self):
        return "<class 'HashTable'>"


new_hashTable = HashTable(5)

new_hashTable.insertion("David")
new_hashTable.insertion("Masupa")
new_hashTable.insertion("Ceaser")
new_hashTable.insertion("Magura")
new_hashTable.insertion("Anthony")

print(new_hashTable.get_table())
