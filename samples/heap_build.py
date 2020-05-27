from math import floor
from typing import List

# create larger class of Heap
# many functions are part of solution skeleton provided by instructor. 
# compare, heapify, build_heap, heappush, heappop, MinHeap, MaxHeap are original code.

class Heap:
    def __init__(self, array: List[int]) -> None: # initialization accepts a list of integers
        self.elements = array # list of ints put into "elements"
        self.size = len(array) # Number of elements in heap
        self.build_heap() # call function build_heap

    # find index of left child of the node at idx
    def left(self, idx: int) -> int: 
        return 2 * idx + 1

    # find index of right child of the node at idx
    def right(self, idx: int) -> int: 
        return 2 * idx + 2

    # find index of parent of the node at idx
    def parent(self, idx: int) -> int: 
        return floor((idx - 1) / 2)

    #swap two nodes in the heap
    def swap(self, idx1: int, idx2: int) -> None: 
        tmp = self.elements[idx1] #load idx1 into temporary node
        self.elements[idx1] = self.elements[idx2] #load idx2 into idx1
        self.elements[idx2] = tmp #load temporary node into idx2

    # convert heap to printable string format
    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        # return empty dashes if no elements
        if self.size == 0:
            return '\\--'
        # otherwise, use string format to build tree structure for every id not exceeding heap size
        elif idx < self.size: 
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    # defines string conversion method, calls to_string
    def __str__(self) -> str:
        return self.to_string()

    # defines length retrieval method, calls size
    def __len__(self) -> str:
        return self.size
    
    # raises error if comparison not implemented for subclasses
    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError
    
    # organizes the heap
    def heapify(self, idx: int) -> None:
        top = idx # top is working node

        # if left node defies rules (top>left or left>top, based on comparison used), top reassigned to left
        if self.left(idx) < self.size and self.compare(self.elements[top], self.elements[self.left(idx)]):
            top = self.left(idx) 

        # if right node defies rules, top reassigned to right
        if self.right(idx) < self.size and self.compare(self.elements[top], self.elements[self.right(idx)]):
            top = self.right(idx) 
        
        # if top has been reassigned, switch nodes so that heap rules are followed
        if top != idx:
            self.swap(idx,top)
            self.heapify(top) # call heapify on the switched node

    # call heapify for all nodes, organizing the heap
    def build_heap(self) -> None:
        for i in range(floor(self.size/2), -1, -1): 
            self.heapify(i)

    #add element to heap
    def heappush(self, key: int) -> None:
        self.elements.append(key) # append to elements
        self.size += 1 # increase size
        self.heapify(self.size) # re-organize

    def heappop(self) -> int:
        self.size = self.size-1 # decrease size
        return self.elements.pop(0) # use pop method

#subclass where root is smallest, with appropriate comparison function 
class MinHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        if a > b:
            return True
        else:
            return False

#subclass where root is largest, with appropriate comparison function
class MaxHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        if a < b:
            return True
        else:
            return False