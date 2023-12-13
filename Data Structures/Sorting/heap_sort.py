
""" heapsort_max (arr)
apply max-heapsort on an unsorted arr
:param arr:
:return: sorted array arr
O (n log n)
"""
def heapsort_max(arr):
    pass


""" heapsort_min (arr)
apply min-heapsort on an unsorted arr
:param arr:
:return: sorted array arr
O (n log n)
"""
def heapsort_min(arr):
    pass



""" parent (pos)
find parent of current position in heap
:param pos:
:return: parent value
O(1)
"""
def parent(pos):
    return pos//2


""" left (pos)
find left child of current position in heap
:param pos:
:return: left child's value
O(1)
"""
def left(pos):
    return 2*pos + 1


""" right (pos)
find right child of current position in heap
:param pos:
:return: right child's value
O(1)
"""
def right(pos):
    return 2*pos + 2


""" max_heapify (arr, pos)
max-heapify the heap
:param arr:
:param pos:
:param heap_size:
:return: boolean for successful heapify
O(log n)
"""
def max_heapify(arr, pos, heap_size):
    l = left(pos)
    r = right(pos)

    # print (l, len(arr))
    # print (arr[l])
    # print (arr[pos])

    # left largest
    if l <= heap_size and arr[l] > arr[pos]:
            largest = l
    else:
        largest = pos
    # right largest
    if r <= heap_size and arr[r] > arr[largest]:
            largest = r
    # if largest isn't current, swap and recursively run 
    if largest is not pos:
        swap(arr, pos, largest)
        max_heapify(arr, largest, heap_size)


""" min_heapify (arr, pos)
min-heapify the heap
:param arr:
:param pos:
:param heap_size:
:return: boolean for successful heapify
O(log n)
"""
def min_heapify(arr, pos, heap_size):
    l = left(pos)
    r = right(pos)

    # left smaller
    if l <= heap_size and arr[l] < arr[pos]:
        smallest = l
    else:
        smallest = pos 
    # right smaller than left and pos
    if r <= heap_size and arr[r] < arr[smallest]:
        smallest = r
    
    # if smallest isn't current, swap and recursively run 
    if smallest is not pos:
        swap(arr, pos, smallest)
        min_heapify(arr, smallest, heap_size)


""" swap (node1, node2)
swap two nodes in the heap
:param arr:
:param node1:
:param node2:
:return: boolean for successful swap
O(1)
"""
def swap(arr, node1, node2):
    arr[node1], arr[node2] = arr[node2], arr[node1]
    

""" build_heap (arr, my_type)
build either a max or min heap depending on type specified
:param arr:
:param heap_size:
:param my_type:
:return: sorted arr using either max or min heapsort
O(n logn)
"""
def build_heap(arr, heap_size, my_type):
    if len(arr) is not 0:
        # max
        if my_type == "max":
            # range end is not inclusive
            for i in range(len(arr)//2, -1, -1):
                max_heapify(arr, i, heap_size)
        # min
        elif my_type == "min":
            for i in range(len(arr)//2, -1, -1):
                min_heapify(arr, i, heap_size)
        # neither 
        else:
            print("Type not specified correctly.")



def main():
    #      0 1 2 3 4 5  6  7  8 9 
    arr = [3,8,1,9,2,10,42,33,0,5]

    #       0 1 2 3 4 5  6  7  8 9
    arr2 = [3,8,1,9,2,10,42,33,0,5] 

    heapsort_max(arr)
    heapsort_min(arr2)

    print(arr)
    print(arr2)


if __name__ == "__main__":
    print ("========== Starting Program ==========")
    main()

