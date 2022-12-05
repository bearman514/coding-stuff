"""_summary_
"""


class Node():

    def __init__(self, data) -> None:
        self.data = data
        self.children = []  # list
        self.parent = None  # optional


def height(tree):
    pass


def size(tree):
    pass


class Traverse():
    """Walking a tree.
    - Recursive are common to solve
    - Tree walks:
        1. DFS (pre-order, in-order, post-order)
        2. BFS
    """

    def depth_first(self):
        """Completely traverse one sub-tree before exploring a sibling sub-tree
        Time complete: O(n)
        """
        pass

    def breadth_first(self):
        """Traverse all nodes at one level before progressing to the next level
        Time complete: O(n)
        """
        pass
