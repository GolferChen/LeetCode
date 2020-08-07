from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Down-Top
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#         # if root.left is None and root.right is None: # No Need in fact
#         #     return 1
#         left_max_depth = self.maxDepth(root.left)
#         right_max_depth = self.maxDepth(root.right)
#         return max(left_max_depth, right_max_depth) + 1

# Top-Down
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.max_depth = 0
        def get_max(node, depth):
            if node is None:
                return
            if node.left is None and node.right is None:
                self.max_depth = max(self.max_depth, depth)
            get_max(node.left, depth+1)
            get_max(node.right, depth+1)
        get_max(root, self.max_depth+1)
        return self.max_depth



