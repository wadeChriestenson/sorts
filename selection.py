import numpy
from numpy.random.mtrand import random
from time import sleep


def selection_sort(lst):
    """
    Selection sort function
    :param lst: List of integers
    """
    z = 1
    # Traverse through all lst elements
    for i in range(len(lst)):
        # Find the minimum element in unsorted lst
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]
        print(lst, ' ', z)
        z += 1
        sleep(.500)


# Driver code to test above
if __name__ == '__main__':
    lst = numpy.random.randint(1, high=100, size=24, dtype=int)
    selection_sort(lst)  # Calling selection sort function

