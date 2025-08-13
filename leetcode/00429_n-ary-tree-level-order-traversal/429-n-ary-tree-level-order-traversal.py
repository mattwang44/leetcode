"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import defaultdict


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        ret = []

        def helper(node, level):
            if len(ret) == level:
                ret.append([])

            ret[level].append(node.val)

            if node.children:
                for child in node.children:
                    helper(child, level + 1)

        helper(root, 0)

        return ret
