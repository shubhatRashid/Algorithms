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
"""