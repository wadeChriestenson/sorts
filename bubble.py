import numpy
from numpy.random.mtrand import random
from time import sleep


def bubble_sort(lst):
    """
      Bubble sort function
      :param lst: lst of unsorted integers
      """
    n = len(lst)
    z = 1
    swapped = False

    # Traverse through all list elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the list from 0 to size of lst - i - 1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                swapped = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                print(lst, '', z)
                z += 1
                sleep(.100)
        if not swapped:
            return


lst = numpy.random.randint(1, high=100, size=24, dtype=int)
bubble_sort(lst)
