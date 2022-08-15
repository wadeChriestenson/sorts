import numpy
from numpy.random.mtrand import random
from time import sleep


def bubble_sort(arr):
    n = len(arr)
    z = 1
    swapped = False

    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr, '', z)
                z += 1
                sleep(.100)
        if not swapped:
            return


arr = numpy.random.randint(1, high=100, size=24, dtype=int)
bubble_sort(arr)
