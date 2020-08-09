from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive Version
# class Solution:
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         if root is None:
#             return False
#         if root.left is None and root.right is None:
#             return root.val == sum
#         return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

# Iterative Version, DFS
# class Solution:
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         stack = deque([(root, sum)])
#         while len(stack) > 0:
#             cur_node, cur_sum = stack.pop()
#             if cur_node is None:
#                 continue
#             if cur_node.left is None and cur_node.right is None and cur_node.val == cur_sum:
#                 return True
#             if cur_node.left:
#                 stack.append((cur_node.left, cur_sum - cur_node.val))
#             if cur_node.right:
#                 stack.append((cur_node.right, cur_sum - cur_node.val))
#         return False

# Iterative Version, BFS
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        queue = deque([(root, sum)])
        while len(queue) > 0:
            cur_node, cur_sum = queue.popleft()
            if cur_node is None:
                continue
            if cur_node.left is None and cur_node.right is None and cur_node.val == cur_sum:
                return True
            if cur_node.left:
                queue.append((cur_node.left, cur_sum - cur_node.val))
            if cur_node.right:
                queue.append((cur_node.right, cur_sum - cur_node.val))
        return False
