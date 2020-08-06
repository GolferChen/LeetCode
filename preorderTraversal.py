from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# # Recursive Version
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         if root is None:
#             return deque([])
#         orders = deque([root.val])
#         if root.left is None and root.right is None:
#             return orders
#         left_orders = self.preorderTraversal(root.left)
#         right_orders = self.preorderTraversal(root.right)
#         orders += left_orders
#         orders += right_orders
#         return orders

# Iteration Version, Wrong
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         if root is None:
#             return []
#         stack = deque([root])
#         visited = deque([root])
#         orders = [root.val]
#         if root.left is None and root.right is None:
#             return orders
#         cur = root.left
#         while len(stack) > 0:
#             while cur and (not (cur in visited)):
#                 orders.append(cur.val)
#                 visited.append(cur)
#                 stack.append(cur)
#                 cur = cur.left
#             cur_tmp = cur
#             if cur is None:
#                 if len(stack) > 0:
#                     parent = stack.pop()
#                     if parent.right is None:
#                         if len(stack) > 0:
#                             parent_2 = stack.pop()
#                             cur = parent_2
#                             cur = cur.left
#                     else:
#                         cur = parent.right
#                         if not (cur is None):
#                             stack.append(cur)
#                             visited.append(cur)
#                             orders.append(cur.val)
#                         cur = cur.left
#             if cur_tmp in visited:
#                 cur = cur_tmp.right
#                 if not (cur is None):
#                     stack.append(cur)
#                     visited.append(cur)
#                     orders.append(cur.val)
#                     cur = cur.left
#         return orders


# # Iteration Version
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         stack = deque([root])
#         # visited = deque([root])  # no need
#         output = []
#         while len(stack) > 0:
#             cur = stack.pop()
#             if not (cur is None): # in case that root is None
#                 if not (cur.right is None): # first right
#                     stack.append(cur.right)
#                 output.append(cur.val)
#                 if not (cur.left is None): # then left
#                     stack.append(cur.left)
#         return output

# Iteration Version, Morris
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        cur = root
        while not (cur is None):
            if cur.left is None:
                output.append(cur.val)
                cur = cur.right
            else:
                predecessor = cur.left
                while not (predecessor.right is None or predecessor.right == cur):
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = cur
                    output.append(cur.val)
                    # cur = predecessor
                    cur = cur.left
                else:
                    predecessor.right = None
                    # output.append(cur.val) # already visited
                    cur = cur.right
        return output

