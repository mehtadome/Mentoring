import sys 
sys.path.append('../')
# import Node class
import Nodes.node as node 

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0    

    # given the object of a stack, print all the values in it
    # O(n)
    def printStack(self):
        print(" --- ")
        top = self.top
        while top is not None:
            print("|", top.val, "|")
            top = top.next
        print(" --- ")


    # given the object of a stack and a value, push it to the top of the stack
    # O(1)
    def push(self, value):
        # empty list
        if self.top is None:
            self.top = node.Node()
            self.top.val = value 
            self.size += 1
            return self

        # create new node
        insert_me = node.Node()
        insert_me.val = value 
        # insert node is new top
        insert_me.next = self.top 
        self.top = insert_me

        return self

    
    # given the object of a stack, pop the top value
    # O(1)
    def pop(self):
        # empty list
        if self.top is None:
            print("The stack is already empty.")
            return None 
        
        # pop the top 
        top = self.top.next 
        # store popped value, set node to None
        old_top = self.top.val
        self.top = None 
        self.top = top  # set new top to next in line
        
        self.size -= 1
        return old_top


    # given the object of a stack, check to see what the top element is
    # O(1)
    def peek(self):
        if self.top is None:
            print("The stack is empty.")
            return self 
        
        return self.top.val
    

    # given the object of a stack, check to see if it is empty 
    # O(1)
    def isEmpty():
        if self.size is 0:
            return True 
        return False


# given the object of a stack and a list of values, push the values to the stack
# O(n)
def create_stack(mystack, values):
    if len(values) is 0:
        self.top = None 
        return self 
    
    for val in values:
        mystack.push(val)
    
    return mystack


# main function for testing class methods
def main():
    # create stack
    mystack = Stack()
    mystack = create_stack(mystack, {0, 1, 2, 3, 4, 5, 6})
    print("My stack is:")
    mystack.printStack()

    # test push
    for i in range(16):
        mystack.push(i)

    print("The new stack after several pushes is:")
    mystack.printStack()

    # test pop
    popped_val = mystack.pop()
    print("The most recently popped value is", popped_val)
    print("The new stack after popping is:")
    mystack.printStack()

    # test peek()
    top_val = mystack.peek()
    print("The topmost value in the stack is", top_val)


if __name__ == "__main__":
    print("Starting Program.")
    main()

