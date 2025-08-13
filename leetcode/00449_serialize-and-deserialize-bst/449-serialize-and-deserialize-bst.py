# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    delimiter = ","

    def postorder(self, root):
        if not root:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        return self.delimiter.join(str(num) for num in self.postorder(root))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if len(data) == 0:
            return None

        nums = [int(val) for val in data.split(self.delimiter)]

        def helper(nums, l=-sys.maxsize, h=sys.maxsize):
            if not nums or nums[-1] < l or nums[-1] > h:
                return None
            val = nums.pop()
            root = TreeNode(val)
            root.right = helper(nums, val, h)
            root.left = helper(nums, l, val)
            return root

        return helper(nums)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
