# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        common_ancestors = []

        def traverse(node):
            nonlocal common_ancestors
            if not node:
                return False, False
            is_q = is_p = False
            if node == p:
                is_p = True
            if node == q:
                is_q = True

            lp, lq = traverse(node.left)
            rp, rq = traverse(node.right)

            if (lp or rp or is_p) and (lq or rq or is_q):
                common_ancestors.append(node)
            return (lp or rp or is_p), (lq or rq or is_q)

        traverse(root)
        return common_ancestors[0]
