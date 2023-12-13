class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0  

    
    def push(self, value):
        # Is the stack empty?

        # Create a new node, save pointer to current top.

        # Update the top of the stack and set next to previous top.
        pass


    def pop(self):
        # Is the stack empty?

        # Delete the node at the top of the stack
        pass


    def peek(self):
        # Is the stack empty?

        # Return the value of the node at the top of the stack
        pass


    def isEmpty(self):
        # Is the stack empty?
        pass


    def size(self):
        # Is the stack empty?
        pass


    def printStack(self):
        # Is the stack empty?
        pass



def main():
    mystack = Stack
    myarr = [1,2,3,4,5,6,7,8,9,10]
    for i in myarr:
        mystack.push(i)

    mystack.peek()
    mystack.pop()
    mystack.printStack()
    mystack.pop()
    mystack.printStack()

    print(mystack.isEmpty())
    print(mystack.size())

    mystack.push(11)
    mystack.printStack()
    mystack.peek()

    
if __name__ == "__main__":
    main()

