"""
    Priority Queue for Sorting the Nodes by frequency and generating the Huffman Tree
"""
import urllib


class SinglyLinkedListNode:

    def __init__(self, freq, char=None, left_child=None, right_child=None):
        """
        :param char: A character to be encoded
        :param freq: A frequency of a character generated
        :param left_child: Reference of the left child
        :param right_child: Reference of the right child
        """
        self.left_child = left_child
        self.right_child = right_child
        self.char = char
        self.freq = freq
        self.Next = None

    def __str__(self):
        return "<class 'Node'>"


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, freq, char=None):
        """
        Time complexity - O(n)
        Space complexity - O(n)
        Auxiliary space - O(1)
        :param char: A character value for a Node
        :param freq: A frequency value for a Node
        :return: None
        """

        # Enqueue when LinkedList in empty
        if self.head is None:
            insert_node = SinglyLinkedListNode(freq, char)

            self.head = insert_node
            self.tail = insert_node
        else:
            insert_node = SinglyLinkedListNode(freq, char)

            # Enqueue at the end of the LinkedList
            if insert_node.freq <= self.tail.freq:
                self.tail.Next = insert_node
                self.tail = insert_node
            else:
                pointer = self.head

                # Enqueue at the head of the LinkedList
                if insert_node.freq >= pointer.freq:
                    insert_node.Next = pointer
                    self.head = insert_node
                    self.size += 1
                    return

                while pointer is not None:

                    # Enqueue in between the LinkedList
                    if insert_node.freq > pointer.Next.freq:
                        insert_node.Next = pointer.Next
                        pointer.Next = insert_node
                        break
                    pointer = pointer.Next

        self.size += 1

    def enqueue_subtree(self, freq, left_child, right_child):
        """

        :param freq: A frequency value for a Node
        :param left_child: A right child for the node being created
        :param right_child: A left child for the node being created
        :return: None
        """
        if self.head is None:
            insert_node = SinglyLinkedListNode(freq)

            insert_node.left_child = left_child
            insert_node.right_child = right_child

            self.head = insert_node
            self.tail = insert_node
        else:

            # Create an instance of a Node with a Left Child and Right Child
            insert_node = SinglyLinkedListNode(freq)
            insert_node.left_child = left_child
            insert_node.right_child = right_child

            if insert_node.freq <= self.tail.freq:
                self.tail.Next = insert_node
                self.tail = insert_node
            else:
                pointer = self.head

                if insert_node.freq >= pointer.freq:
                    insert_node.Next = pointer
                    self.head = insert_node
                    self.size += 1
                    return

                while pointer is not None:
                    if insert_node.freq > pointer.Next.freq:
                        insert_node.Next = pointer.Next
                        pointer.Next = insert_node
                        break
                    pointer = pointer.Next

        self.size += 1

    def dequeue(self):
        """
        time-complexity: O(n)
        auxiliary-space: O(1)
        space-complexity: O(1)

        Note: 'n' is the number of nodes in the LinkedList

        :return: Value with the least frequency in the priority queue
        """
        pointer = self.head

        # Return None is LinkedList is empty
        if self.head is None:
            return

        # Return Node at every instance
        leaf_node = self.tail
        while pointer is not None:

            if pointer is self.tail:
                self.head = None
                self.tail = None
                break

            elif pointer.Next is self.tail:
                pointer.Next = None
                self.tail = pointer
                break
            else:
                pointer = pointer.Next

        self.size -= 1
        return leaf_node

    def file_opener(self, path):
        """
        time-complexity: O(1)
        space_complexity: O(1)

        :param path: The path of a file to compress
        :return: A string of context in the file
        """

        my_file_handle = urllib.request.urlopen(path)

        return my_file_handle.read()

    def file_writer(self, path, message):
        """

        :param path: The path of the file we intend to write to
        :param message: A message we intend to write into a file
        :return: None
        """

        my_file_handle = open(path, "w")

        my_file_handle.write(message)

        my_file_handle.close()

    def generate_freq_table(self, message):
        """
        time-complexity: O(m)
        auxiliary-space: O(m)
        space-complexity: O(1)

        Note: 'm' is the number of unique characters in the message

        :param message: A message who's character method will calculate frequency values
        :return: A frequency table
        """

        frequency_table = dict()

        unique_characters = set(message)

        # Loop through unique characters checking frequency in message
        for char in unique_characters:
            frequency_table[char] = message.count(char)

        return frequency_table

    def generate_tree(self, message):
        """
        time-complexity: O(n-1)
        auxiliary-space: O(1)
        space-complexity: O(1)

        Note: 'n' is the number of nodes in the LinkedList

        Loops through the Priority Queue to generate a Huffamn Tree
        :return: Huffman Tree
        """

        # Generate a frequency table for the message
        frequency_table = self.generate_freq_table(message)

        # Enqueue every unique char from the frequency table into a priority queue
        for char in frequency_table:
            self.enqueue(frequency_table[char], char)

        while self.size != 1:

            left_child = self.dequeue()
            right_child = self.dequeue()

            frequency = left_child.freq + right_child.freq

            self.enqueue_subtree(frequency, left_child, right_child)

        return self

    def _generate_codes_helper(self, tree, list):
        """
        time-complexity: lg base 2 of n
        auxiliary-space:
        space-complexity:

        :param tree: A huffman tree
        :param list: An empty list to inside rough codes
        :return: None
        """
        if tree.char is not None:
            list.append(tree.char)

            temp_list = []

            for i in list:
                if type(i) is int or type(i) is str:
                    temp_list.append(i)

            list.pop()
            list.pop()
            list.append(temp_list)
            return
        else:

            list.append(0)
            self._generate_codes_helper(tree.left_child, list)

            list.append(1)
            self._generate_codes_helper(tree.right_child, list)
            if type(list[-3]) is int:
                list.pop(-3)

    def generate_codes(self, tree):
        """

        :param tree: A huffman Tree
        :return: A Huffman code table for a message
        """

        code = []

        self._generate_codes_helper(tree, code)

        # Code table
        code_table = dict()

        index = 0
        for i in code:
            if type(i) is list:
                codes = ""
                char = code[index][-1]
                for j in code[index]:
                    if type(j) is int:
                        codes += str(j)
                code_table[char] = codes

            else:
                pass
            index += 1

        return code_table

    def encode(self, code_table, message):
        """
        time-complexity: O(n)
        auxiliary-space:
        space-complexity:

        :param code_table: A huffman code table
        :param message: A message to encode
        :return: an encoded message
        """

        message_encode = ""

        count = 0
        # Looping through the entire message character by character
        while count < len(message):
            char = message[count]
            code = code_table[char]

            message_encode += str(code)

            count += 1

        return message_encode

    def decode(self, tree, encoded_message):
        """

        :param tree: A huffman tree
        :param encoded_message: An encoded message
        :return: The actual message
        """

        original_message = ""

        for code in encoded_message:
            pointer = code


"""
    Test 1    
"""
Queue = SinglyLinkedList()

path = '/Users/readingtechnology/Documents/college/Computer Science - Year 2/Term - 2/Data Structures and Algorithms/' \
       'test_file.txt'

# # Message extracted from a text file
# file_info = Queue.file_opener(path)
#
# # Passing message to generate frequency table
# Frequency_table = Queue.generate_freq_table(file_info)
#
# # Passing message to generate Huffman Tree
# Huffman_tree = Queue.generate_tree(file_info)


"""
    Test to generate the Huffman tree
    
    Status: Works
    
    Note - Test this using a word in place of the path above
"""
Huffman_tree = Queue.generate_tree("ab ab cab")


"""
    Test to generate codes
    
    Status: Works
"""
huffman_code_table = Queue.generate_codes(Huffman_tree.head)


"""
    Test to encode a message 
    
    Status: Works
"""
encode = Queue.encode(huffman_code_table, "ab ab cab")

print(encode)


"""

"""
