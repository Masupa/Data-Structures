"""
    Implementation of the Bubble sort algorithm
"""


def bubble_sort(arr):
    """
    time-complexity: O(n**2)
    space-complexity: O(1)
    auxiliary-complexity: O(1)
    
    :param arr: an array of integers
    :return: a sorted array in ascending order
    """

    index1 = 0
    while index1 < len(arr):

        index2 = 0
        while index2 < len(arr) - index1:

            if index2 < (len(arr) - 1) and arr[index2] > arr[index2 + 1]:
                x = arr[index2]
                arr[index2] = arr[index2 + 1]
                arr[index2 + 1] = x

            index2 += 1

        index1 += 1

    return arr


sort_arr = [10, 500, 28, 10, 2, 4, 0, 24]

print(bubble_sort(sort_arr))
