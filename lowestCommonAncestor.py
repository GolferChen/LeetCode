from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Wrong
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if root is None:
#             return root
#         self.nearest_node = None
#         self.find = False
#         self.p = p
#         self.q = q
#         self.visited = deque([(root, root.left)])
#         self.run(root, root.left, root)
#         if not ((root, root.right) in self.visited):
#             self.run(root, root.right, root)
#         self.run(root.left, root.right, root)
#         return self.nearest_node
#     def run(self, node_1, node_2, nearest_node):
#         if self.find:
#             return
#         if node_1 == node_2:
#             return
#         if node_1 in [self.p, self.q] and node_2 in [self.p, self.q]:
#             self.nearest_node = nearest_node
#             self.find = True
#         if node_1:
#             self.run(node_1, node_1.left, node_1)
#             self.run(node_1, node_1.right, node_1)
#             self.run(node_1.left, node_2.right, node_1)
#         if node_2:
#             self.run(node_2, node_2.left, node_2)
#             self.run(node_2, node_2.right, node_2)
#             self.run(node_2.left, node_2.right, node_2)
#         if node_1 and node_2:
#             self.run(node_1.left, node_2.left, nearest_node)
#             self.run(node_1.left, node_2.right, nearest_node)
#             self.run(node_1.right, node_2.left, nearest_node)
#             self.run(node_1.right, node_2.right, nearest_node)
#             self.run(node_1, node_2.left, nearest_node)
#             self.run(node_1, node_2.right, nearest_node)
#             self.run(node_2, node_1.left, nearest_node)
#             self.run(node_2, node_1.right, nearest_node)


# Recursive, bottom up
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         def run(node):
#             if node is None:
#                 return False
#             if self.nearest_node:
#                 return False
#             left_state = run(node.left)
#             right_state = run(node.right)
#             if left_state and right_state:
#                 self.nearest_node = node
#             if (left_state or right_state) and (node.val == p.val or node.val == q.val):
#                 self.nearest_node = node
#             return left_state or right_state or (node.val == p.val or node.val == q.val)
#         if root is None:
#             return root
#         self.nearest_node = None
#         run(root)
#         return self.nearest_node

# Version Two. Store parent Node
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def update_map(node):
            if node is None:
                return
            if node.left:
                # self.parent_map[node.left] = node
                self.parent_map[node.left.val] = node
                update_map(node.left)
            if node.right:
                # self.parent_map[node.right] = node
                self.parent_map[node.right.val] = node
                update_map(node.right)
        if root is None:
            return root
        # self.parent_map = {root: None}
        self.parent_map = {root.val: None}
        update_map(root)
        ## for p
        cur_node = p
        visited = deque()
        while cur_node:
            # visited.append(cur_node)
            visited.append(cur_node.val)
            # cur_node = self.parent_map[cur_node]
            cur_node = self.parent_map[cur_node.val]
        ## for q
        cur_node = q
        while cur_node:
            # if cur_node in visited:
            if cur_node.val in visited:
                return cur_node
            # visited.append(cur_node)
            visited.append(cur_node.val)
            # cur_node = self.parent_map[cur_node]
            cur_node = self.parent_map[cur_node.val]
        # return None




