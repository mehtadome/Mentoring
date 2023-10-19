import sys 
import math

# implemented as a simple MaxHeap
class MaxHeap:
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


    """ insert (self, insert_me)
    insert the value 'insert_me' to end of heap
    :param self:
    :param insert_me:
    :return: boolean if true or false
    O(1)
    """
    def insert(self, insert_me):
        # first insert to array
        self.size += 1
        self.heap[self.size-1] = insert_me
        
        if self.size is not 1:
            self.heapify(self.size-1)


    """ heapify (self, pos)
    heapify upon insertion || primary used by insert()
    :param self:
    :param pos: 
    :return: boolean for successful heapify
    O(1) to O(log n)
    """
    def heapify(self, pos):
        # get index of parent
        padre = self.parent(pos)
        # if parent is smaller than current child
        if padre <= self.size and self.heap[padre] > self.heap[pos]:
            # swap using index of current el and index of parent
            self.swap(pos, padre)
            # recurse on old index of parent
            self.heapify(padre)


    """ max_heapify (self)
    max-heapify the heap
    :param self:
    :return: max of heap
    O(log n)
    """
    def max_heapify(self, pos):
        l = self.left(pos)
        r = self.right(pos)

        #if l<= self.size and r<= self.size:
            #print("Comparing: left=", self.heap[l], "right", self.heap[r], "current", self.heap[pos])

        # left larger
        if l <= self.size and self.heap[l] > self.heap[pos]:
            largest = l
        # set current to largest
        else:
            largest = pos
            #print("My current position of", self.heap[pos], "index of" ,pos, "is largest")
        # check if right > left or right > pos
        if r <= self.size and self.heap[r] > self.heap[largest]:
            largest = r
         
        # if largest isn't current, swap and recursively run 
        if largest is not pos:
            #print("Swapped", self.heap[pos], "with", self.heap[largest])
            self.swap(pos, largest)
            self.max_heapify(largest)

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


    """ extract_max (self)
    find and remove the current max from the MaxHeap
    replace max with furthest right node and max_heapify from top-down
    :param self:
    :return: current maximum
    O(log n)
    """
    def extract_max(self):
        mymax = self.heap[0]

        # swap lastmost child with root (aka min)
        self.swap(0, self.size)
        # min is now last child
        del self.heap[self.size] 
        self.size -= 1

        # run reverse heapify on now unsorted minheap 
        self.max_heapify(0)
        return mymax


    """ height (self)
    find the height of the given heap
    :param self:
    :return: integer of the height
    O(1)
    """
    def height(self):
        return math.floor(math.log(self.size, 2)) + 1
    

    """ print_heap (self)
    print heap contents in array format
    :param self:
    :return: void
    O(log n)
    """
    def print_heap(self):
        print("\nPrinting Heap:")
        for i in range(0, self.size+1):
            print (self.heap[i], end=" ")
        print("\n=======\n")


""" build_max_heap (self, values)
build the heap
:param self:
:param values:
:return: sorted max-heap
O(log n)
"""
def build_max_heap(myheap):
    if myheap.size is 0:
        # range end is not inclusive
        for i in range(myheap.size//2, -1, -1):
            myheap.max_heapify(i)


def main():
    arr = [1,5,0,3,2,10,15,6,600]
    # pass in array and heap.size of len(arr)-1 to account for 0index
    my_heap = MaxHeap(arr, len(arr)-1)
    my_heap.print_heap()

    print ("Sorting heap")
    build_max_heap(my_heap)
    my_heap.print_heap()
    #my_heap.insert(100)

    my_height = my_heap.height()
    print("Heap's height is", my_height)
    
    mymax = my_heap.extract_max()
    print("Heap's current max is", mymax)
    my_heap.print_heap()

if __name__ == "__main__":
    print ("========== Starting Program ==========")
    main()

        
        