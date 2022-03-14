# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def helper(node, curr):
            nonlocal count
            if not node:
                return
            if node.val >= curr:
                count += 1

            curr = max(curr, node.val)
            helper(node.left, curr)
            helper(node.right, curr)

        helper(root, root.val)
        return count

    # BFS interative
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        q = [(root, root.val)]
        while q:
            node, val = q.pop()
            if not node:
                continue
            if node.val >= val:
                count += 1

            new_val = max(node.val, val)
            q.append((node.left, new_val))
            q.append((node.right, new_val))
        return count
