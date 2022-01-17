# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # time O(N), space O(N)
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        memo = {}

        def helper(root):
            if not root:
                return 1

            height = max(helper(root.right) + 1, helper(root.left) + 1)
            if height not in memo:
                memo[height] = []
            memo[height].append(root.val)
            return height

        helper(root)
        return memo.values()
