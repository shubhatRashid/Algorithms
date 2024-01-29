"""
Heap:
    - A heap is a complete binary tree.
    - In a heap all the descendants are either greater than the current element(max heap)
        or smaller than the current element (min heap).
    - A heap stays a complete binary tree even after insertion of a new node or deletion
        of a node.
    - A pop operation on heap gives max element (max-heap) or min element (min-heap) from
        the heap.The operation takes olog(n) time complexity (for heapifying)
    - Similarly inserting an element also takes olog(n) time complexity.
    - Use heapq library in python for list type min heaps implementation
    - Use heapq library in python for list type max heaps implementation by
      turning number data into opposite sign(* -1)
"""
import heapq

minHeap = [5,2,6,4,5,7,9] # initialising a list as our min heap
heapq.heapify(minHeap)  # heapifying
print(minHeap)  # returns [2, 4, 6, 5, 5, 7, 9]
heapq.heappush(minHeap,10)
print(minHeap) # returns [2, 4, 6, 5, 5, 7, 9, 10]
heapq.heappop(minHeap)
print(minHeap) # returns [4, 5, 6, 5, 10, 7, 9]

maxHeap = [-9,-7,-5,-4,-6,-2,-5]
# all other operations are same
