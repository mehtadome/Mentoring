import sys 
import math


"""
Heaps - Largest element is at the top.
"""
class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0


    """
    HEAP EXAMPLE

                50
        30              15
    19      20      10      5

    REPRESENTED AS AN ARRAY
    [50, 30, 15, 19, 20, 10, 5]
    """


    """ parent (self, pos)
    find parent of current position in heap
    :param self:
    :param insert_me:
    :return: parent value
    O(1)
    """
    def parent(self, pos):
        # How can i use math on the index to refer to the parent?
        pass


    """ left (self, pos)
    find left child of current position in heap
    :param self:
    :param insert_me:
    :return: left child's value
    O(1)
    """
    def left(self, pos):
        # How can i use math on the index  to refer to the left child?
        pass
    

    """ right (self, pos)
    find right child of current position in heap
    :param self:
    :param insert_me:
    :return: right child's value
    O(1)
    """
    def right(self, pos):
        # How can i use math on the index to refer to the right child?
        pass
    

    """ insert (self, insert_me)
    insert the value 'insert_me' using current index
    :param self:
    :param insert_me:
    :param i:
    :return: boolean if successful
    O(1)
    """
    def insert(self, insert_me, i):
        # How do i add an element to an array?

        # Heapify must occur on every insertion. 
        # Heaps must maintain structure my definition.
        pass


    """ heapify (self, pos)
    heapify upon insertion
    :param self:
    :param pos: 
    :return: boolean for successful heapify
    O(1) to O(log n)
    """
    def heapify(self, pos):
        # get parent
        padre = self.parent(pos)
        # is parent less than current position

        # if so, swap and heapify
        pass

    
    """ max_heapify (self)
    max-heapify the heap
    :param self:
    :return: boolean for successful heapify
    O(log n)
    """
    def max_heapify(self, pos):
        l = self.left(pos)
        r = self.right(pos)

        # left larger

        # right larger

        # target is our position
        
        # if largest isn't current, swap and recursively run 
        pass


    """ swap (self, node1, node2)
    swap two nodes in the heap
    :param self:
    :param node1:
    :param node2:
    :return: boolean for successful swap
    O(1)
    """
    def swap(self, node1, node2):
        # basic swap
        pass


    """ sorted (self)
    determine if heap is sorted
    :param self:
    :return: position where heap is not sorted
    """
    def sorted(self, pos=0):
        # check if left is larger than current
        # check if right is larger than current
        # if neither, return current position
        pass
 

    """ height (self)
    find the height of the given heap
    :param self:
    :return: integer of the height
    """
    def height(self):
        # How do i use math to find the height?
        pass
    

    """ create_heap (self, values)
    create a heap from a given set of values
    :param self:
    :param values: 
    :return: correctly ordered max-heap
    """ 
    def create_heap (self, values):
        # create the heap using heapify
        pass
        
        
import heapq
first = lambda h: 2**h - 1      # H stands for level height
last = lambda h: first(h + 1)
level = lambda heap, h: heap[first(h):last(h)]
prepare = lambda e, field: str(e).center(field)
def hprint(heap, width=None):
    if width is None:
        width = max(len(str(e)) for e in heap)
    height = int(math.log(len(heap), 2)) + 1
    gap = ' ' * width
    for h in range(height):
        below = 2 ** (height - h - 1)
        field = (2 * below - 1) * width
        print(gap.join(prepare(e, field) for e in level(heap, h)))


def main():
    myheap = Heap()
    myheap.create_heap([1,2,3,4,5,6,7,8,9,10])
    hprint(myheap.heap)


if __name__ == "__main__":
    main()
    print("\n")
    exit()


"""
LC Problems

Easy: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/
"""