import sys 
import math

# largest element is at top
# creates a separate heap from array of values
class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0


    """ parent (self, pos)
    find parent of current position in heap
    :param self:
    :param insert_me:
    :return: parent value
    O(1)
    """
    def parent(self, pos):
        return pos//2


    """ left (self, pos)
    find left child of current position in heap
    :param self:
    :param insert_me:
    :return: left child's value
    O(1)
    """
    def left(self, pos):
        return 2*pos
    

    """ right (self, pos)
    find right child of current position in heap
    :param self:
    :param insert_me:
    :return: right child's value
    O(1)
    """
    def right(self, pos):
        return 2*pos + 1
    

    """ insert (self, insert_me)
    insert the value 'insert_me' using current index
    :param self:
    :param insert_me:
    :param i:
    :return: boolean if true or false
    O(1)
    """
    def insert(self, insert_me, i):
        # first insert to array
        self.heap.append(insert_me)
        self.size += 1

        if self.size is not 1:
            self.heapify(i)


    """ heapify (self, pos)
    heapify upon insertion
    :param self:
    :param pos: 
    :return: boolean for successful heapify
    O(1) to O(log n)
    """
    def heapify(self, pos):
        padre = self.parent(pos)
        if self.heap[padre] < self.heap[pos]:
            self.swap(pos, padre)
            self.heapify(padre)
    

    """ max_heapify (self)
    max-heapify the heap
    :param self:
    :return: boolean for successful heapify
    O(log n)
    """
    def max_heapify(self, pos):
        # will need to make sure there is no index-out-of-bounds
        l = self.left(pos)
        r = self.right(pos)

        # left larger
        if l <= self.size and self.heap[l] > self.heap[pos]:
            largest = l
        # right larger
        elif r <= self.size and self.heap[r] > self.heap[pos]:
            largest = r
        else:
            largest = pos 
        
        # if largest isn't current, swap and recursively run 
        if largest is not pos:
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


    """ sorted (self)
    determine if heap is sorted
    :param self:
    :return: position where heap is not sorted
    """
    def sorted(self, pos=0):
        if self.size is not <= 1:
            if self.heap[self.left(pos)] < pos and self.heap[self.right(pos)] < self.heap[pos]:
                self.sorted(self.left(pos))
                self.sorted(self.right(pos))
            else:
                return pos


    """ height (self)
    find the height of the given heap
    :param self:
    :return: integer of the height
    """
    def height(self):
        return math.floor(math.log(self.size, 2)) + 1
    

    """ create_heap (self, values)
    create a heap from a given set of values
    :param self:
    :param values: 
    :return: correctly ordered max-heap
    """ 
    def create_heap (self, values):
        if len(values) is not 0:
            for i in range(len(values)):
                insert_me = values[i]
                self.insert(insert_me, i)
        
        


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


