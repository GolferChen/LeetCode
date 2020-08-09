from collections import deque
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive Version
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if root is None:
#             return True
#         return self.is_two_tree_symmetric(root.left, root.right)
#
#     def is_two_tree_symmetric(self, tree_1, tree_2):
#         if (tree_1 is None and tree_2) or (tree_2 is None and tree_1):
#             return False
#         if tree_1 is None and tree_2 is None:
#             return True
#         if tree_1.val != tree_2.val:
#             return False
#         return self.s_two_tree_symmetric(tree_1.left, tree_2.right) and self.s_two_tree_symmetric(tree_1.right, tree_2.left)

# Iterative Version, Wrong, Passing 194/195
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # if root is None:
        #     return True
        queue = deque([(1, root)])
        stack = deque()
        while len(queue) > 0:
            cur_level, cur_node = queue.popleft()
            if cur_node:
                queue.append((cur_level+1, cur_node.left))
                queue.append((cur_level+1, cur_node.right))
            stack_content = (cur_level, cur_node.val) if cur_node else (cur_level, math.inf)
            if len(stack) <= 0:
                stack.append(stack_content)
            else:
                stack_top = stack[-1]
                if stack_top == stack_content:
                    stack.pop()
                else:
                    stack.append(stack_content)
        return len(stack) == 1

# Iterative Version
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        queue = deque([root.left, root.right])
        while len(queue) > 0:
            node_1 = queue.popleft()
            node_2 = queue.popleft()
            if (node_1 is None and node_2) or (node_2 is None and node_1):
                return False
            if node_1 and node_2 and node_1.val != node_2.val:
                return False
            if node_1 and node_2:
                queue.append(node_1.left)
                queue.append(node_2.right)
                queue.append(node_1.right)
                queue.append(node_2.left)
        return True

