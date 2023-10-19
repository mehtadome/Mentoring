import sys 
import math

# implemented as a min-priority queue
# will keep order more efficiently when extracting min (heap[0])
class MinHeap:
    def __init__(self, heap=[], size=0):
        self.heap = heap
        self.size = size


    """ parent (self, pos)
    find parent of current position in heap
    :param self:
    :return: parent value
    O(1)
    """
    def parent(self, pos):
        return pos//2


    """ left (self, pos)
    find left child of current position in heap
    :param self:
    :return: left child's value
    O(1)
    """
    def left(self, pos):
        return 2*pos + 1
    

    """ right (self, pos)
    find right child of current position in heap
    :param self:
    :return: right child's value
    O(1)
    """
    def right(self, pos):
        return 2*pos + 2


    """ heap_minimum(self)
    returns the minimum of the heap
    :param self:
    :return: minimum
    O(1)
    """
    def heap_minimum(self):
        return self.heap[0]
    

    """ heap_extract_min (self)
    find and remove the current min from the MinHeap
    replace min with furthest right node and min_heapify
    :param self:
    :return: current minimum
    """
    def heap_extract_min(self):
        assert self.size > 0; "Heap underflow."

        mymin = self.heap[0]
        # swap lastmost child with root (aka min)
        self.swap(0, self.size)
        # min is now last child
        del self.heap[self.size] 
        self.size -= 1

        # run reverse heapify on now unsorted minheap 
        self.min_heapify(0)
        return mymin


    """ min_heapify (arr, pos)
    min-heapify the heap
    :param self:
    :param pos:
    :return: accurately returns sorted min-heap
    O(log n)
    """
    def min_heapify(self, pos):
        l = self.left(pos)
        r = self.right(pos)

        # left smaller
        if l <= self.size and self.heap[l] < self.heap[pos]:
            smallest = l
        else:
            smallest = pos 
        # right smaller than left and pos
        if r <= self.size and self.heap[r] < self.heap[smallest]:
            smallest = r
        
        # if smallest isn't current, swap and recursively run 
        if smallest is not pos:
            self.swap(pos, smallest)
            self.min_heapify(smallest)


    """ heap_decrease_key (self, pos, key)
    compares and continues, exchanging keys if element's is smaller
    :param self:
    :param pos:
    :param key: 
    :return: returns sorted heap with correctly ordered keys 
    O(log n)
    """
    def heap_decrease_key(self, pos, key):
        assert key < self.heap[pos]; "New key is larger than current key"
        # set current position to new key
        self.heap[pos] = key 
        # keep exchanging keys if parent > current pos
        while pos > 0 and self.heap[self.parent(pos)] > self.heap[pos]:
            # swap current position with parent's position
            self.swap(pos, self.parent(pos))
            # set new position to parent
            pos = self.parent(pos)
    

    """ min_heap_insert(self, key)
    insert key of new element and then min_decrease_key() it
    :param self:
    :param key:
    :return: returns sorted heap with correctly ordered keys
    O(log n)
    """
    def min_heap_insert(self, key):
        #print ("inserting", key)
        self.size += 1
        self.heap[self.size] = float("inf")
        self.heap_decrease_key(self.size, key)


    """ swap (self, node1, node2)
    swap two nodes in the heap
    :param self:
    :param node1:
    :param node2:
    :return: boolean for successful swap
    O(1)
    """
    def swap(self, node1, node2):
        self.heap[node1], self.heap[node2] = self.heap[node2], self.heap[node1]


    """ height (self)
    find the height of the given heap
    :param self:
    :return: integer of the height
    """
    def height(self):
        print (self.size)
        return math.floor(math.log(self.size, 2)) + 1
    

    """ print (self)
    print order of the heap
    :param self:
    """
    def print_heap(self):
        print ("Printing Heap:")
        for i in range(self.size):
            print (self.heap[i], end = " ")
        print ("\n")


""" build_min_heap (self, values)
build heap using insert function
:param arr:
:return: sorted min-heap
O(log n)
"""
def build_min_heap(arr, myheap):
    myheap.size = -1
    # have to pre-set heap to size of array length
    myheap.heap = [0] * len(arr)
    # range end is not inclusive
    for i in arr:
        myheap.min_heap_insert(i)

def main():
    arr = [99, 25, 76, 69, 80, 66, 11, 13]
    # pass in array and heap.size of len(arr)-1 to account for 0index
    my_heap = MinHeap()
    build_min_heap(arr, my_heap)
    my_heap.print_heap()

    
    my_heap.print_heap()

    #my_height = my_heap.height()
    #print("Heap's height is", my_height)
    
    mymin = my_heap.heap_extract_min()
    print("Heap's current min is", mymin, "\n")
    my_heap.print_heap()


if __name__ == "__main__":
    print ("========== Starting Program ==========")
    main()

        
        


    


