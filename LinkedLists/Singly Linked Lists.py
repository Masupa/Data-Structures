"""

"""


class Node:

    def __init__(self, data):
        self.Data = data
        self.Next = None

    def __str__(self):
        return "<class 'Node'>"


class SinglyLinkedList:

    # Constructor initialized with no initial link, but with a head and tail referencing None
    def __init__(self):
        self.Head = None
        self.Tail = None
        self.size = 0

    def append(self, value):
        """
            Appends an item at the end of the Singly Linked List
        :param value: value of any type
        :return: None
        """
        append_node = Node(value)

        # Appends to end when list is empty
        if self.Head is None:
            self.Head = append_node
            self.Tail = append_node
        # Appends to tail when list is not empty
        else:
            self.Tail.Next = append_node
            self.Tail = append_node
        self.size += 1

    """ Method inserts an element at a given position // Head has position 0, next to head position 1"""
    def insert(self, position, value):
        """
            Inserts an item into the Singly Linked List at a given position, where the head has position 0,
            head's next has position 1, and so on
        :param position: int in the range(0, (size_of_list - 1))
        :param value: value of any type
        :return: None
        """
        insert_node = Node(value)

        # Insertion at the head Node
        if position == 0:
            insert_node.Next = self.Head
            self.Head = insert_node
            self.size += 1

        elif position > self.size:
            print("Index error - Index is out of range")
            return None

        else:
            pointer = self.Head
            counter = 0
            while pointer is not None:
                if counter == (position - 1):
                    insert_node.Next = pointer.Next
                    pointer.Next = insert_node
                    self.size += 1
                    if position == self.size - 1:
                        self.Tail = insert_node
                    break
                else:
                    counter += 1
                    pointer = pointer.Next

    def pop(self):
        """
            Method pops out the last item in the Singly Linked List
        :param self:
        :return: Value that was popped
        """
        counter = 1
        pointer = self.Head
        while pointer is not None:
            if counter == (self.size - 1):
                popped_item = pointer.Next
                pointer.Next = None
                self.Tail = pointer
                self.size -= 1
                return popped_item.Data
            else:
                counter += 1
                pointer = pointer.Next

    def delete(self, value):
        pointer = self.Head

        if pointer.Data is value:
            self.Head = pointer.Next
            pointer.Next = None
            self.size -= 1
        else:
            while pointer is not None:
                if pointer.Next.Data is value:
                    delete_node = pointer.Next
                    pointer.Next = delete_node.Next
                    delete_node.Next = None
                    self.size -= 1
                    return None
                else:
                    pointer = pointer.Next

            print("Value does not exist in the Singly Linked List")


test_lst = SinglyLinkedList()
test_lst.append(1)
test_lst.append(2)
test_lst.append(3)

test_lst.insert(0, 0)
test_lst.insert(3, 2.5)
test_lst.insert(5, 4)

test_lst.append(5)

test_lst.delete(3)
