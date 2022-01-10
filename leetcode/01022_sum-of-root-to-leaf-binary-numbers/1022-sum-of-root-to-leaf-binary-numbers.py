# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def traverse(node, accumulate):
            nonlocal ret
            accumulate = accumulate * 2 + node.val
            if not (node.left or node.right):
                ret += accumulate
            else:
                if node.left:
                    traverse(node.left, accumulate)
                if node.right:
                    traverse(node.right, accumulate)

        traverse(root, 0)
        return ret
