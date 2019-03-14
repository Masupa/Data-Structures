"""
    ReadMe:
        - Implementation improves the "Basic Imple 1" by handling resolution collision through a linked list
"""


# *** Implementation of the Singly Linked List leveraging on the Node concept *** ///

# Node class
class Node:

    # Constructor :- Node object will be instantiated with data and no pointer to next None
    def __init__(self, value):
        self.DataVal = value
        self.NextVal = None

    # Data value getter
    def get_value(self):
        return self.DataVal

    # Next pointer getter
    def get_next(self):
        return self.NextVal

    def __str__(self):
        return "<class 'Node'>"


# Singly Linked List class
class LinkedList:

    # Constructor instantiated with no head
    def __init__(self):
        self.head = None
        self.size = 0

    # Insertion at the tail - Application to Hash Tables
    def tail_insert(self, element):
        insertion_node = Node(element)

        pointer = self.head
        if pointer is None:
            self.head = insertion_node
            self.size += 1
            return None

        while pointer.NextVal is not None:
            pointer = pointer.NextVal

        pointer.NextVal = insertion_node
        self.size += 1

    # Deletion of a node in the LinkedList given data value
    def deletion(self, element):
        # Edges Cases - Deleting at the head, at the tail, or in between the head and tail
        pointer = self.head

        # Deleting the head
        if pointer.DataVal is element:
            deletion_node = self.head
            self.head = deletion_node.NextVal
            deletion_node.NextVal = None
            self.size -= 1
            return None

        while pointer is not None:
            if pointer.NextVal is None:
                break
            else:
                if pointer.NextVal.DataVal is element:
                    deletion_node = pointer.NextVal
                    pointer.NextVal = deletion_node.NextVal
                    deletion_node.NextVal = None
                    self.size -= 1
                    return deletion_node

            pointer = pointer.NextVal

        return "Element not in the LinkedList"

    # Searching for an element in the LinkedList
    def search(self, element):
        first_pointer = self.head
        second_pointer = first_pointer.NextVal

        if first_pointer.DataVal is element:
            return "Found"

        while second_pointer is not None:
            if second_pointer.DataVal is element:
                return first_pointer.DataVal
            first_pointer = first_pointer.NextVal
            second_pointer = second_pointer.NextVal

        return "Not found"

    # Display utilizes a list to show items in the Linked List
    def display(self):
        display_list = list()

        pointer = self.head
        while pointer is not None:
            display_list.append(pointer.DataVal)
            pointer = pointer.NextVal

        return display_list

    def __str__(self):
        return "<class 'LinkedList'>"


# HashTable class
class HashTable:

    # Constructor initialized with a size of a Hash Table
    def __init__(self, table_size):
        self.size = table_size
        self.lst = LinkedList()
        self.table = [None] * self.size

    # Basic Hash Function that looks considers input as int or str
    def __hash_function(self, item):
        # Edges cases of the import - Either int, str or something else

        # int case
        if type(item) is int:
            return item % self.size

        # Str case
        elif type(item) is str:
            hash_sum = 0
            for i in range(len(item)):
                hash_sum = hash_sum + ord(item[i])
            return hash_sum % self.size

        # Other cases - Will be worked on later
        else:
            print("Either cases have not been considered yet")

    def insertion(self, item):
        # Calling the Hash Function to get the hash_value
        hash_value = self.__hash_function(item)

    def __str__(self):
        return "<class 'Hash Table'>"


new_hash_table = HashTable(5)

new_hash_table.insertion(1)
new_hash_table.insertion(6)
