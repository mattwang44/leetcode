# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive, time O(N), space O(N)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ret = self.postorderTraversal(root.left)
        ret.extend(self.postorderTraversal(root.right))
        ret.append(root.val)

        return ret

    # Iterative, time O(N), space O(N)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ret = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return ret[::-1]
