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
                else:
                    print("cycle found")

        print(result)

# FINDING PATH BETWEEN TWO VERTICES IN DIRECTED GRAPH
    # graph is adjacency dictionary format
    def has_path(graph, src, dst):
        def dfs(graph, src, dst):
            if src == dst:
              return True

              for nbr in graph[src]:
                if dfs (graph, nbr, dst):
                   return True
            return False

        return dfs (graph, src, dst)

# FINDING PATH BETWEEN TWO VERTICES IN AN UNDIRECTED GRAPH
    # graph is adjacency list format
    """
        edges = [
                ('i', 'j'),
                ('k', 'i'),
                ('m', 'k'),
                ('k', 'l'),
                ('o', 'n')
            ]
    """
def undirected_path(edges, node_A, node_B):
    adj = {}
    for u, v in edges:
        if u in adj:
            adj[u].append (v)
        else:
            adj[u] = [v]

        if v in adj:
            adj[v].append (u)
        else:
            adj[v] = [u]

    visited = set ()

    def dfs(node_A, node_B):
        if node_A == node_B:
            return True
        visited.add (node_A)
        for nbr in adj[node_A]:
            if nbr not in visited and dfs (nbr, node_B):
                return True
        return False

    return dfs (node_A, node_B)

# TOPOLOGICAL SORT IN DIRECTED GRAPHS #
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
def topologicalSort(graph):
     # if graph is not in adjacency list format then convert it
     visited = set()
     result = []
     def dfs(vertex):
         if vertex not in visited:
            visited.add(vertex)
            for nbr in graph[vertex]:
                dfs(nbr)
            result.insert(0,vertex)
         #else:
         # detect cycle
     for key in list(graph.keys()):
         dfs(key)

     return result

#print(topologicalSort(graph=mygraph))
#example
# course schedule II on leetcode
def findOrder(numCourses,prerequisites):
    prelist = {i: [] for i in range (numCourses)}
    for c, p in prerequisites:
        prelist[c].append (p)

    result = []
    visited = set ()

    def dfs(crs):
        if crs in visited:
            return False

        if prelist[crs] == []:
            if crs not in result:
                result.append (crs)
            return True

        visited.add (crs)
        for pre in prelist[crs]:

            if not dfs (pre):
                return False

        visited.remove (crs)
        prelist[crs] = []
        result.append (crs)
        return True

    for key in list (prelist.keys ()):
        if not dfs (key):
            return []
    return result






