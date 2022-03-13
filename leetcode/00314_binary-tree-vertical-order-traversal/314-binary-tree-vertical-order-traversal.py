# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        left = []
        right = []
        center = []

        q = deque([(root, 0)])
        while q:
            node, level = q.popleft()
            if level == 0:
                center.append(node.val)
            else:
                ret = left if level < 0 else right
                if len(ret) == abs(level) - 1:
                    ret.append([])

                ret[abs(level) - 1].append(node.val)

            if node.left:
                q.append((node.left, level - 1))
            if node.right:
                q.append((node.right, level + 1))

        return left[::-1] + [center] + right
