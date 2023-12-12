# Pseudocode
Heaps are based in the fundamentals of positioning / indexing. Also, recall that the largest element of a max-heap is at the top.

## ```Heap()``` class
A ```Heap``` has two attributes, a ```heap``` in the form of a list, and a ```size```.

## Tasks
Implement the following helper methods for the ```Heap``` class:
1. ```parent(position)``` - Find parent of current position in the heap.
2. ```left(position)``` - Find left child of current position.
3. ```right(position)``` - Find right child of current position.
4. ```insert(value)``` - Insert a value into the heap.
5. ```heapify()``` - Heapify the heap.
6. ```max_heapify()``` - Max heapify the heap.
7. ```swap(val1, val2)``` - Swap two positions in the heap.
8. ```sorted()``` - Returns the position where heap is _not_ sorted.
9. ```height()``` - Returns the height of the heap.
10. ```delete()``` - Delete the root of the heap.
11. ```create_heap(values)``` - Create the heap with an array of values. 

#### Optional
```min_heapify(position)``` - Min heapify the heap.

### Clarifications
The method names provided are not the way you must create them as. ```heapify()``` is inherently recursive indicating that passing in no parameters is incorrect.

## Challenge Yourself
```heapsort(values)``` - Given an array of unsorted values, sort it. 
