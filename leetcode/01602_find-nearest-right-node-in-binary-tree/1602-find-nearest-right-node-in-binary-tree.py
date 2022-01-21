# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        is_target = False
        target_level = 0
        q = deque([(root, 1)])
        while q:
            node, level = q.popleft()

            if is_target:
                return node if target_level == level else None

            if node.val == u.val:
                is_target = True
                target_level = level

            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
