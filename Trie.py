"""
TRIE DATA STRUCTURE :
- Also known as prefix tree.
- A tree like data structure used to store strings. The idea
  is to put string with same prefix in similar branch.Trie makes
  searching strings with common prefixes easier like the autocomplete suggestions that
  pop while using google search box or the spell checker in keyboards.

  image : "https://media.geeksforgeeks.org/wp-content/uploads/20220828232752/Triedatastructure1.png"

- Unlike binary tree a trie node can have any number of children.
- The ability of trie to tell us if a string in it start with a substring given
    is what makes trie special otherwise storing and grabbing strings can also
    be done with hashmaps.
"""


class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = Node ()

    def insert(self, word: str) -> None:
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = Node ()
            curr = curr.children[s]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for s in word:
            if s not in curr.children:
                return False
            curr = curr.children[s]

        if curr.endOfWord == True:
            return True
        else:
            return False
