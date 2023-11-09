class Node:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class LinkedList:

    # create the list
    def __init__(self):
        self.head = None
        self.count = 0

    # prints the list
    def echo(self):
        ptr = self.head
        arr = []
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        print(arr)

    def getValue(self, index: int) -> int:
        # return index
        x=1

    def addAtHead(self, val: int) -> None:
        # add value to the head. new value should be new head of linked list.
        x=1

    def addAtTail(self, val: int) -> None:
        # add after current tail
        x=1

    def addAtIndex(self, index: int, val: int) -> None:
        # given an index, place a new node after it.
        x=1

    def deleteAtIndex(self, index: int) -> None:
        # delete the node at given index.
        x=1

    def max(self) -> int:
        # return the greatest value in the list
        x=1


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