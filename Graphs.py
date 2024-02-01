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

mygraph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['A','E'],
    'D' : ['B','E','F'],
    'E' : ['C','B','D','F'],
    'F' : ['D','E']
}

class Graph: # dictionary or adjacency list representation
    def __init__(self,gdic = None):
        if gdic:
            self.gdic = gdic
        else:
            self.gdic ={}

    def addEdge(self,vertex,edge):
        self.gdic[vertex].append(edge)

    def traversal(self,vertex,method):
        visited = set(vertex)

        # using set instead of list due to its
        # high efficiency in finding elements
        # from it becoz under the hood sets
        # are created using hashmaps

        storage = [vertex]
        # queue for bfs and stack for dfs
        result = []
        while storage:
            curr = storage.pop(0)
            result.append(curr)
            for adjacent in self.gdic[curr]:
                if adjacent not in visited:
                    if method == 'dfs':
                        storage.insert(0,adjacent)
                    else:
                        storage.append(adjacent)
                    # append for bfs and insert for dfs
                    visited.add(adjacent)
        print(result)

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

graph = Graph(gdic=mygraph)
graph.traversal('A','bfs')




