class Node:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


class LinkedList:
    # create the list
    def __init__(self):
        self.head = None
        self.count = 0


    # override len
    def __len__(self):
        return self.count


    # prints the list
    def echo(self):
        ptr = self.head
        # using the pointer, traverse and print each value

        # when do we stop?


    # get value at certain index
    def getValue(self, index: int) -> int:
        # is index larger than our length?
        
        # index is 0-based, length is 1-based
        pass


    # add a node in front of the head
    def addAtHead(self, val: int) -> None:
        # is LL empty?
        # else, add at head
        pass


    # insert a node with given val
    def insert(self, val: int) -> None:
        # is LL empty?
        # else, insert
        pass

    
    # delete a node with given val
    def delete(self, val: int) -> None:
        # is LL empty?
        # else, delete
        pass


    # add a node after the tail
    def addAtTail(self, val: int) -> None:
        # is LL empty?
        # else, add at tail
        #       what unique trait does the tail have?
        pass

    
    # add a node at a given index
    def addAtIndex(self, index: int, val: int) -> None:
        # is LL empty?

        # is index larger than our length?

        # is index 0?

        # else, add at index
        pass


    # delete the node at the index given
    def deleteAtIndex(self, index: int) -> None:
        # is LL empty?

        # is index larger than our length?

        # is index 0?

        # else, delete at index
        pass


    # return the greatest value in the list  
    def max(self) -> int:
        ptr = self.head
        # traverse to find max
        # when do we stop?
    

    # return the greatest value in the list
    def min(self) -> int:
        ptr = self.head
        # traverse to find min
        # when do we stop?



def createLists():
    myLL1 = LinkedList()
    # node values 1
    nv1 = [i for i in range(1, 11, 2)]
    while nv1:
        myLL1.addAtHead(nv1.pop()) 
    
    myLL2 = LinkedList()
    # node values 2
    nv2 = [i for i in range(2, 21, 3)]
    while nv2:
        myLL2.addAtHead(nv2.pop())
    
    return myLL1, myLL2


def main():
    myLL1, myLL2 = createLists()
    print ("LinkedLists created:")
    myLL1.echo()
    myLL2.echo()

    print("\nmyLL1 2nd index is", myLL1.getValue(2), "and 4th index is", myLL1.getValue(4))
    print("\nmyLL1 1st index is", myLL2.getValue(1), "and 5th index is", myLL2.getValue(5))

    print("\nmyLL1 has a new head!")
    myLL1.addAtHead(100)
    myLL1.echo()
    print("myLL2 has a new head!")
    myLL2.addAtHead(666)
    myLL2.echo()

    print("\nmyLL1 has a new tail!")
    myLL1.addAtTail(314)
    myLL1.echo()
    print("myLL2 has a new tail!")
    myLL2.addAtTail(421)
    myLL2.echo()

    print("\nNew value of -103456 added at 3rd index of myLL1!")
    myLL1.addAtIndex(3, -103456)
    myLL1.echo()
    print("New value of 103456 added at 9th index of myLL2!")
    myLL2.addAtIndex(9, 103456)
    myLL2.echo()

    print("\nGreatest value in myLL1 is", myLL1.max())
    print("\nGreatest value in myLL2 is", myLL2.max())

    print ("\nDeleting myLL1 3rd index:")
    myLL1.deleteAtIndex(3)
    myLL1.echo()
    print ("\nDeleting myLL2 0th index:")
    myLL2.deleteAtIndex(0)
    myLL2.echo()



if __name__ == "__main__":
    print ("Beginning of program.\n")
    main()
    print ("\nEnd of program.")

