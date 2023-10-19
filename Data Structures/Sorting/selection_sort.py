# Selection Sort: sorts the array by constantly finding the min
# O(n^2)
# [5, 2, 6, 4, 1, 3]
def selection_sort(arr):
    # check for len(1) arr
    if len(arr) is not 1:
        i = 0
        j = 1
        while i < len(arr):
            # new min is current el of first loop
            my_min = arr[i]
            # index is default to new min
            my_min_i = i
            # find minimum in array
            while j < len(arr):
                # if el is less than current min
                if arr[j] <= my_min:
                    my_min = arr[j]
                    my_min_i = j
                j += 1
            # perform the swap if changes happened
            if my_min_i is not i:
                arr[my_min_i] = arr[i]
                arr[i] = my_min
            # incrememnt sorted arrays counter
            i += 1
            # reset j to after the sorted array
            j = i+1


arr = [5,2,6,4,1,3]
selection_sort(arr)
print(arr)