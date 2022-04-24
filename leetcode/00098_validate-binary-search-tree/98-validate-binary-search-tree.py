# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, lower, upper):
            if not node:
                return True

            if not lower < node.val < upper:
                return False

            l = helper(node.left, lower, node.val)
            r = helper(node.right, node.val, upper)

            return l and r

        return helper(root, -sys.maxsize, sys.maxsize)
