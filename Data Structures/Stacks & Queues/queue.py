import sys 
sys.path.append('../')
# import Node class
import Nodes.node as node 

# FIFO: First In, First Out
class Queue:
    def __init__(self):
        self.top = None 
        self.size = 0
    
    
    # given the object of a queue, print its contents
    # O(n)
    def printQueue(self):
        print(" --- ")
        top = self.top
        while top is not None:
            print("|", top.val, "|")
            top = top.next
        print(" --- ")
    

    # given the object of a queue, insert a node of specified value in it
    # O(n)
    def enqueue(self, value):
        # empty list
        if self.top is None:
            self.top = node.Node()
            self.top.val = value 
            return self

        insert_me = node.Node()
        insert_me.val = value

        top = self.top
        while (top.next != None):
            top = top.next
        top.next = insert_me

        # return the new root of the queue
        self.size += 1
        return self
    

    # given the object of queue, delete the topmost element
    # O(1)
    def deque(self):
        # empty queue
        if self.top is None:
            print("The queue is already empty.")
            return None
        
        # save old top value
        nxt = self.top.next
        top = self.top.val
        self.top = None
        # set top to next in line
        self.top = nxt 

        self.size -= 1
        return top


    # given the object of a queue, peek the topmost element 
    # O(1)
    def peek(self):
        # empty queue
        if self.top is None:
            print("The queue is empty.")
            return None 
        # return the value of front in line
        return self.top.val


    # given the object of a queue, check if it is empty
    # O(1)
    def isEmpty(self):
        if self.size is 0:
            return True 
        return False

# given the object of a queue and a list of values, add each value to the queue
def create_queue(myqueue, values={}):
    # empty list
    if len(values) is 0:
        myqueue.top = node.Node() 
        return myqueue
    
    for val in values:
        myqueue.enqueue(val)
    
    return myqueue
    

# main function for testing methods
def main():
    # create the queue
    myqueue = Queue()
    myqueue = create_queue(myqueue, {0,2,4,6,8})
    print("The queue consists of:")
    myqueue.printQueue()

    # enqueue test
    for i in range(5):
        myqueue.enqueue(i%2)
    print("The updated queue after several enqueues is:")
    myqueue.printQueue()

    # deque test
    dequed_val = myqueue.deque()
    print("The most recent dequed value is", dequed_val)
    print("The queue after the deque is:")
    myqueue.printQueue()

    # peek test
    top_most = myqueue.peek()
    print("The first in line in the queue is", top_most)

    # isEmpty test
    print("T/F: The queue is empty.", myqueue.isEmpty())

if __name__ == "__main__":
    print("Starting Program.")
    main()