# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive, time O(N), space O(N)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ret = self.inorderTraversal(root.left)
        ret.append(root.val)
        ret.extend(self.inorderTraversal(root.right))
        return ret

    # Iterative, time O(N), space O(N)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ret = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            ret.append(curr.val)
            curr = curr.right

        return ret
