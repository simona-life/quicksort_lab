from enum import Enum
import time
import sys


def str_to_array(array):
    return [int(i) for i in array.split(',')]


def quicksort(array, type, with_tracker=False):
    less = []
    equal = []
    greater = []
    i = 0
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                i += 1
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                i += 1
                greater.append(x)
        if 'asc' == type:
            if len(less + equal + greater) == len(array) and with_tracker:
                return quicksort(less, type) + equal + quicksort(greater, type), i
            return quicksort(less, type) + equal + quicksort(greater, type)
        if 'desc' == type:
            if len(less + equal + greater) == len(array) and with_tracker:
                return quicksort(greater, type) + equal + quicksort(less, type), i
            return quicksort(greater, type) + equal + quicksort(less, type)
    else:
        return array


if __name__ == '__main__':
    input_array = sys.argv[1]
    sort_type = sys.argv[2]
    start_time = time.time()
    input_array = str_to_array(input_array)
    output_array = quicksort(input_array, sort_type, True)
    print(f'array = {output_array[0]}')
    print(f'time = {time.time() - start_time}')
    print(f'Comparisons = {output_array[1]}')
