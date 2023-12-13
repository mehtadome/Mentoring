from random import Random
import time

"""
Implement Bubble Sort. 
"""

# O(n^2)
def bubble_sort(arr):
    pass


start = time.time()
r = Random()
arr = []
for i in range(10000):
    # 0 to one mill
    arr.append(r.randint(0, 1000000))

print (bubble_sort(arr))
end = time.time()

print(end-start)
