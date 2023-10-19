# O(n) sorting algorithm that sorts by creating a constantly growing arr of sorted elements
# and comparing each new one against ones in sorted arr
def insertion_sort(arr):
    i = 1
    sorted_index = 0

    while i < len(arr):

        while arr[i] < arr[sorted_index] and sorted_index >= 0:
            print("Comparing", arr[i], "with", arr[sorted_index])
            sorted_index -= 1
        
        # push to first element
        if sorted_index is -1:
            temp = arr[i]
            del arr[i]
            arr = [temp] + arr
        # push to correct order
        else:
            temp = arr[i]
            del arr[i]
            arr = arr[0:sorted_index+1] + [temp] + arr[sorted_index+1:]

        i += 1
        sorted_index = i-1

    print(arr)


arr = [6, 5, 3, 1, 8, 7, 2, 4]
insertion_sort(arr)
print(arr)