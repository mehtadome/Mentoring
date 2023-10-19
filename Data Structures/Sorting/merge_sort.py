import sys


# helper method for merge_sort
# performs the comparisons and reassignments on the original array
def merge(arr, low, mid, high):
    # low to mid
    lc = arr[low : mid+1]   # left copy
    # mid + 1 => high
    rc = arr[mid+1 : high+1]    # right copy

    # tells when comparisons need to stop
    lc.append(sys.maxsize)
    rc.append(sys.maxsize)

    lc_iterator = 0
    rc_iterator = 0
    sorted_index = low 
    # make sure it stays in relative window
    while sorted_index <= high:
        # if el of left is < than right
        if lc[lc_iterator] < rc[rc_iterator]:
            # set value from og array to lc[lc_i]
            arr[sorted_index] = lc[lc_iterator]
            # iterate
            lc_iterator += 1
        # if el of left is >= right
        else:
            # set value from og array to rc[rc_i]
            arr[sorted_index] = rc[rc_iterator]
            # iterate
            rc_iterator += 1
        # iterate through og array
        sorted_index += 1


# n log(n) sorting algorithm that behaves like a binary tree in its
# recursive-based method of splitting and sorting
def merge_sort(arr, low, high):
    if low >= high:
        return 
    mid = (low + high) // 2     # floor division
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)


arr = [8,2,7,6,9,3,4,1,0,5]
merge_sort(arr, 0, len(arr)-1)
print(arr)





