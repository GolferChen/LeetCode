from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursion Version
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         # output = []
#         if root is None:
#             return []
#         if root.left is None and root.right is None:
#             return [root.val]
#         o_left = self.postorderTraversal(root.left)
#         o_right = self.postorderTraversal(root.right)
#         output = o_left + o_right + [root.val]
#         return output

# Iteration Version
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = deque([root])
        output = []
        visited = deque()
        while len(stack) > 0:
            cur = stack[-1]
            if cur:
                if (cur.left is None or cur.left in visited) and (cur.right is None or cur.right in visited):
                    stack.pop()
                    output.append(cur.val)
                    visited.append(cur)
                else:
                    if cur.right and not (cur.right in visited):
                        stack.append(cur.right)
                    if cur.left and not (cur.left in visited):
                        stack.append(cur.left)
            else:
                stack.pop()
        return output
