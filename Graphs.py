"""
GRAPHS:

- A graph is a nonlinear data structure consisting of nodes(vertices)
    which are connected using edges(arcs).The nodes can be connected
    in any order.
- A city can be considered as graph where all the lanes are
    edges/arcs which connect the junctions of the city which
    represent as nodes/vertices.

GRAPH TERMINOLOGIES:

- Vertices : Nodes of graph.
- Edges : connecting lines between nodes.
- UnWeighted Graph : Edges do not have any weights associated with them.
- Undirected Graph : Edges do not have directions associated with them.
- Cyclic Graph : contains at least one loop.
- Tree : Special type of graph which is acyclic,Unweighted and directed.

TYPES OF GRAPHS :
- Directed :
        Weighted
            positive
            negative
        Unweighted

- Undirected :
        Weighted
            positive
            negative
        Unweighted

REPRESENTATION :
- Adjacency matrix(2d matrix which depicts links between vertices.
- Adjacency list(a list stores vertices and a linked list is used to
    store its edge connections)
- In python we use a nested list to create adjacency matrix and dictionary
    to create adjacency list.
"""

class Graph: # dictionary or adjacency list representation
    def __init__(self,gdic = None):
        if gdic:
            self.gdic = gdic
        else:
            self.gdic ={}
    def addEdge(self,vertex,edge):
        self.gdic[vertex].append(edge)


"""
Graph :
                A 
              /   \
             B     C             
             |  \  |
             D ___ E             
              \   /
                F
"""
mygraph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['A','E'],
    'D' : ['B','E','F'],
    'E' : ['C','B','D','F'],
    'F' : ['D','E']
}
graph = Graph(gdic=mygraph)
print(graph.gdic)


