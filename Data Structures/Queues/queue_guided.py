class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def enqueue(self, data):
        # Is the queue empty?

        # Create new node.

        # Set tail to be new node.

        # Set new tail prev to old tail.
        pass


    def dequeue(self):
        # Is the queue empty?

        # Remove head

        # Set Queue's new head.
        pass


    def peek(self):
        # Return value of Queue's head
        pass


    def size(self):
        # Return size of Queue
        pass


    def isEmpty(self):
        # Return True if Queue is empty, False otherwise
        pass


    def clear():
        # Dequeue() all elements in the queue.
        pass


    def printQueue(self):
        # Is the queue empty?
        #   If so, print "Queue is empty."

        # If not, print "Queue contains: " val
        pass


def main():
    myQueue = Queue()
    myarr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in myarr:
        myQueue.enqueue(i)
    

    print(myQueue.peek())
    print(myQueue.size())
    print(myQueue.isEmpty())


    if not myQueue.isEmpty:
        myQueue.clear()
    myQueue.printQueue()



if __name__ == "__main__":
    main()