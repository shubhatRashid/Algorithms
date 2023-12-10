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
    stack = [root]
    result = []
    while stack:
        temp = stack[0]
        result.append(temp.val)
        if temp.left:
            stack.append(temp.left)
        if temp.right:
            stack.append(temp.right)
        temp = stack.pop(0)
    return result
# dft(a) prints [a,b,c,d,e,f]



