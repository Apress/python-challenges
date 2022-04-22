# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import random
import sys
import time
import numpy as np

from ch09_search_and_sort.solutions.ex06_quick_sort import quick_sort_inplace
from ch09_search_and_sort.intro.intro_insertion_sort import insertion_sort

list_of_values = [random.randrange(10_000) for _ in range(10)]
print(list_of_values)

list_of_values = [random.randrange(1_000_000) for _ in range(1_000_000)]
array_of_values = np.array(list_of_values)

print("list size", sys.getsizeof(list_of_values))
print("array size", sys.getsizeof(array_of_values))

start = time.process_time()
quick_sort_inplace(list_of_values)
end = time.process_time()

print("list sort took %.2f ms" % ((end - start) * 1000))


start = time.process_time()
quick_sort_inplace(array_of_values)
end = time.process_time()

print("array sort took %.2f ms" % ((end - start) * 1000))

start = time.process_time()
insertion_sort(array_of_values)
end = time.process_time()

# für vorsortierte
print("insertion_sort sorted took %.2f ms" % ((end - start) * 1000))

list_of_values = [random.randrange(1_000_000) for _ in range(1_000_000)]
start = time.process_time()
insertion_sort(list_of_values)
end = time.process_time()

print("insertion_sort unsorted list took %.2f ms" % ((end - start) * 1000))

#
#[2388, 4627, 3154, 2827, 8197, 4117, 517, 721, 985, 8795]
#list size 8697456
#array size 8000096
#list sort took 4269.44 ms
#array sort took 9987.83 ms
