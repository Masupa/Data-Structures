"""
    Test code for the Function
"""


"""
    Test 1 - Enqueue and Dequeue of the Node
"""
Queue = SinglyLinkedList()

Queue.enqueue(2, ' ')
Queue.enqueue(1, 'c')
Queue.enqueue(3, 'b')
Queue.enqueue(3, 'a')

# Test 1 of Dequeue

# Queue.dequeue()
# Queue.dequeue()
# Queue.dequeue()
# Queue.dequeue()
#
# # Test 1 of Dequeue when LinkedList is empty
# Queue.dequeue()

"""
    Test generate tree
"""

# Queue.generate_tree()

"""
    Test generate frequency table
"""
text = "ab ab cab"
print(Queue.generate_freq_table(text))

"""
    Test 2 - Building of the Huffman Tree
"""

# Left_child = Queue.dequeue()  # This is a Node
# Right_child = Queue.dequeue()  # This is a Node too
#
# Frequency = Left_child.freq + Right_child.freq
#
# # First enqueue of a subtree
# Queue.enqueue_subtree(Frequency, Left_child, Right_child)
#
# Left_child = Queue.dequeue()
# Right_child = Queue.dequeue()
#
# Frequency = Left_child.freq + Right_child.freq
#
# # Second enqueue of a subtree
# Queue.enqueue_subtree(Frequency, Left_child, Right_child)
#
# Left_child = Queue.dequeue()
# Right_child = Queue.dequeue()
#
# Frequency = Left_child.freq + Right_child.freq
#
# # Third enqueue of a subtree
# Queue.enqueue_subtree(Frequency, Left_child, Right_child)
