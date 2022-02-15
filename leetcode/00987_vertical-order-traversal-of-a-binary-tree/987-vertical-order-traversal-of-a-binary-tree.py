# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        curr_min_col = 0
        q = deque([(root, 0, 0)])
        ret = {}

        while q:
            node, row, col = q.popleft()
            if not ret:
                ret[col] = {row: [node.val]}
            elif col in ret:
                temp = ret[col].get(row, [])
                temp.append(node.val)
                ret[col][row] = temp
            else:
                ret[col] = {row: [node.val]}

            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))

        r = []
        for key_col in sorted(ret):
            temp = []
            for key_row in sorted(ret[key_col]):
                ret[key_col][key_row].sort()
                temp.extend(ret[key_col][key_row])
            r.append(temp)

        return r
