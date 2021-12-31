# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = 0

        def findMinMaxChildValue(root):
            nonlocal max_diff
            l_max = r_max = l_min = r_min = root.val
            if root.left:
                l_min, l_max = findMinMaxChildValue(root.left)
                max_diff = max(abs(root.val - l_max), abs(root.val - l_min), max_diff)
            if root.right:
                r_min, r_max = findMinMaxChildValue(root.right)
                max_diff = max(abs(root.val - r_max), abs(root.val - r_min), max_diff)

            return min(root.val, l_min, r_min), max(root.val, l_max, r_max)

        findMinMaxChildValue(root)
        return max_diff
