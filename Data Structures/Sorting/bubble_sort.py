from random import Random
import time

# O(n^2)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    # arrays will maintain their changes from a function
    return arr


start = time.time()
r = Random()
arr = []
for i in range(10000):
    # 0 to one mill
    arr.append(r.randint(0, 1000000))

print (bubble_sort(arr))
end = time.time()

print(end-start)
