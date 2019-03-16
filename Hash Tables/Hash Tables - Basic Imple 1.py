"""
    ReadMe:
        - This is a basic implementation of the Hash Table with factors in Collision Resolution using linear probing

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
            # Remainder Method
            return item % self._size
        else:
            ord_sum = 0
            for i in range(len(item)):
                ord_sum += ord(item[i])
            # Remainder Method
            return ord_sum % self._size

    def insertion(self, item):
        hash_value = self._hash_function(item)

        # If slot is empty, add item into that slot
        if self.table[hash_value] is None:
            self.table[hash_value] = item
        else:
            index_shifter = hash_value + 1  # Variable to check the next slot
            break_count = 1  # Variable to count beak out of function after checking all slots

            # Reset index_shifter to zero(0) after checking last slot
            if index_shifter > (self._size - 1):
                index_shifter = 0

            # While the next slot is not empty
            while self.table[index_shifter] is not None:
                # Reset index_shifter to zero(0) after checking last slot
                if index_shifter >= (self._size - 1):
                    index_shifter = 0
                else:
                    index_shifter += 1
                    # Move aware of function when we've looped through all slots
                    if break_count >= self._size:
                        print("The Hash Table is out of open slots")
                        print(" ")
                        return None
                break_count += 1
            self.table[index_shifter] = item

    def deletion(self, item):
        # hash_value stores location of item
        hash_value = self._hash_function(item)

        # Reset location to "None" when item is at location
        if self.table[hash_value] is item:
            self.table[hash_value] = None
        else:
            index_shifter = hash_value + 1
            break_det = 0

            if index_shifter >= (self._size - 1):
                index_shifter = 0

            while self.table[index_shifter] is not item:
                if index_shifter >= (self._size - 1):
                    index_shifter = -1
                else:
                    if break_det >= (self._size - 1):
                        print("The value does not exist in the Hash Table")
                        return None
                index_shifter += 1
                break_det += 1

            self.table[index_shifter] = None

    def search(self, item):
        # Hash_value to determine the address of an item
        hash_value = self._hash_function(item)

        # Return address when found in initial hash_value
        if self.table[hash_value] is item:
            return str(item) + " is at the address " + str(hash_value)
        else:
            index_shifter = hash_value + 1
            break_det = 0

            # Reset index_shifter to zero(0) in the case searching after last slot
            if index_shifter == self._size:
                index_shifter = 0

            while self.table[index_shifter] is not item:
                # Reset index_shifter to zero(0) when 1 less than size of hash table
                if index_shifter == (self._size - 1):
                    index_shifter = 0
                else:
                    if break_det == self._size:
                        print(str(item) + " is not in the Hash Table")
                        return None
                break_det += 1
                index_shifter += 1

            return str(item) + " is at the address " + str(hash_value)

    def __str__(self):
        return "<class 'HashTable'>"


new_hashTable = HashTable(10)

new_hashTable.insertion("David")
new_hashTable.insertion("Masupa")
new_hashTable.insertion("Ceaser")
new_hashTable.insertion("Magura")
new_hashTable.insertion("Anthony")
new_hashTable.insertion("Chikumbi")
new_hashTable.insertion("Love")
new_hashTable.insertion("Lydia")
new_hashTable.insertion("Joseph")
new_hashTable.insertion("Peter")

print(new_hashTable.get_table())

new_hashTable.deletion("David")
new_hashTable.deletion("Love")
new_hashTable.deletion("Peter")
new_hashTable.deletion("Chikumbi")

# Case where an item does not exist in the Hash Table
new_hashTable.deletion("PC")

print(new_hashTable.get_table())

print(new_hashTable.search("Masupa"))
print(new_hashTable.search("Love"))
print(new_hashTable.search("Lydia"))
