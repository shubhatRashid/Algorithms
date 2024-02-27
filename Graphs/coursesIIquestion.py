"""
QUESTION : 01
There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1. You are given an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must take course bi first if you
want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have
to first take course 1.
Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.


"""

def findOrder(numCourses, prerequisites):
    if not prerequisites:
        return [i for i in range (numCourses)]

    adj = {i: [] for i in range (numCourses)}
    for u, v in prerequisites:
        adj[u].append (v)

    result = []
    visited = set ()

    def dfs(k):
        if adj[k] == []:
            if k not in result:
                result.append (k)
            return True

        if k in visited:
            return False

        visited.add (k)

        for n in adj[k]:
            if not dfs (n):
                return False
        visited.remove (k)
        adj[k] = []
        result.append (k)
        return True

    for key in adj:
        if not dfs (key):
            return []

    return result

numCourses = 2
prerequisites = [[0,1]]
print(findOrder(numCourses,prerequisites))