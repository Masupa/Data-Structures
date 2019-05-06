"""
    Implementation of the selection sort algorithm
"""


def selection_sort(arr):
    """
    time-complexity: O(n**2)
    space-complexity: O(1)
    auxiliary-complexity: O(1)

    :param arr: an array to be sorted
    :return: an array sorted in ascending order
    """

    # Pointer pointing at the end of the sorted list
    pointer1 = 0
    while pointer1 < len(arr) - 1:

        # Pointer determines the beginning of the unsorted sublist
        pointer2 = 1
        while pointer2 < len(arr):

            if arr[pointer2 - 1] < arr[pointer2]:
                pass
            else:
                min_value = arr[pointer2]

                # Swapping items
                x = arr[pointer2 - 1]
                arr[pointer2 - 1] = min_value
                arr[pointer2] = x

            pointer2 += 1

        pointer1 += 1

    return arr


sort_arr = [10, 500, 28, 10, 2, 4, 0, 24]

print(selection_sort(sort_arr))
