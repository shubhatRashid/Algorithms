"""
Backtracking :
- The algorithm which allows us to get more than one solution to
  a problem using recursive approach.

- The diff between brute force and backtracking is that backtracking can
    eliminate solutions which are not required while brute force gives all
    solutions.

- The solutions to the problem can be represented by a tree
  representation called state space tree.

- The condition which breaks the recursive cycle is called bounding
  condition or function.

- The key difference between recursion and backtracking is that :
    -> Recursion is a function calling itself with simpler arguments each time untill it reaches a
       solution or a boundry

    -> Backtracking is used to find a solution/solutions among all possibilities of a problem.

    -> Unlike recursion the problem is doesnot get smaller at each cycle but all  valid possibilities
       are checked

example :
- Given an array of distinct integers candidates and a target integer target,
  return a list of all unique combinations of candidates
  where the chosen numbers sum to target. You may return
  the combinations in any order.

solution :
"""


def combinationSum(candidates, target) :
    res = []

    def dfs(subset, i, total): # recursive function

        if i > len (candidates) - 1: # bounding condition
            return

        if total > target: # bounding condition
            return

        if total == target: # found solution
            res.append (subset[:])

        subset.append (candidates[i]) # choosing an element
        dfs (subset, i, total + candidates[i])

        subset.pop () # not deciding to choose an element
        dfs (subset, i + 1, total)

        return res