from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Simple Version, using queue
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if root is None:
#             return root
#         queue = deque([(1, root)])
#         pre_node = None
#         pre_level = 0
#         while len(queue) > 0:
#             cur_level, cur_node = queue.popleft()
#             if pre_node:
#                 if cur_level == pre_level:
#                     pre_node.next = cur_node
#                 else:
#                     pre_node.next = None
#             pre_node = cur_node
#             pre_level = cur_level
#             if cur_node.left:
#                 queue.append((cur_level+1, cur_node.left))
#             if cur_node.right:
#                 queue.append((cur_level+1, cur_node.right))
#         cur_node.next = None
#         return root


# Using Queue
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if root is None:
#             return root
#         queue = deque([root])
#         while len(queue) > 0:
#             size = len(queue)
#             pre_node = None
#             for i in range(size):
#                 cur_node = queue.popleft()
#                 if cur_node.right:
#                     queue.append(cur_node.right)
#                 if cur_node.left:
#                     queue.append(cur_node.left)
#                 cur_node.next = pre_node
#                 pre_node = cur_node
#         return root


# Not using queue, for perfect tree
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root:
#             return root
#         root.next = None
#         left_most_node = root
#         while left_most_node.left:
#             cur_node = left_most_node
#             while cur_node:
#                 cur_node.left.next = cur_node.right
#                 cur_node.right.next = cur_node.next.left if cur_node.next else None
#                 cur_node = cur_node.next
#             left_most_node = left_most_node.left
#         return root


# Not using queue, for general tree, self implemented
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        root.next = None
        left_most_node = root
        continue_flag = True
        # while left_most_node.left or left_most_node.right:
        while continue_flag:
            continue_flag = False
            cur_node = left_most_node
            while cur_node:
                # if cur_node.left is None and cur_node.right is None:
                #     cur_node = cur_node.next
                #     continue
                if cur_node.left and cur_node.right:
                    cur_node.left.next = cur_node.right
                    node = cur_node.right
                elif cur_node.left:
                    node = cur_node.left
                elif cur_node.right:
                    node = cur_node.right
                else:
                    cur_node = cur_node.next
                    continue
                continue_flag = True
                # node.next = self.get_next_left_most(cur_node.next) if cur_node.next else None
                node.next = self.get_next_left_most(cur_node.next)
                cur_node = cur_node.next
            left_most_node = self.get_next_left_most(left_most_node)
        return root

    def get_next_left_most(self, left_most_node):
        if left_most_node is None:
            return left_most_node
        cur_node = left_most_node
        while cur_node:
            if cur_node.left:
                return cur_node.left
            if cur_node.right:
                return cur_node.right
            cur_node = cur_node.next
        return None

