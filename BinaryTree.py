"""
Binary Tree :
    A data struction consisting of nodes where each node has atmost
    two children generally represented as left and right.Node with
    no parent is called Root and node with no children is called leaf.
    A binary tree has :
        - almost 2 children
        - a unique path towards each node
"""


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


# CREATE NODES
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

# LINK THE NODES
a.left = b
a.right = c

b.left = d
b.right = e

c.left = f

# prints   a
#         /  \
#        b     c
#       / \     \
#      d   e     f

"""
Depth First Traversal :
    Traversing the tree by going in depth first and then laterally.
    Can be done either using iteration of recursion
"""

# DFT using iteration
def dft(root):
    if not root:
        return []
    stack = [root] #stack
    result = []
    while stack:
        temp = stack.pop()
        result.append(temp.val)
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)
    return result

# DFT using recursion
def dftr(root):
    if not root:
        return []
    res = []
    res.append(root.val)
    left = dftr(root.left)
    right = dftr(root.right)
    res += left
    res += right
    return res

"""
Breadth First Traversal :
    Traversing the tree by going in breadth first and then vertically.
    Can be done either using iteration of recursion
"""
# BFT using iteration
def bft(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        temp = queue.pop(0)
        result.append (temp.val)

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

    return result

'''
Important Note :
    - recursion uses stack under the hood and hence bfs 
        cannot be implemented using recursion as it uses 
        queue
'''
