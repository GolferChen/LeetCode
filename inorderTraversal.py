from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        orders = []
        stack = [root]
        cur = root
        visited = []
        while len(stack) > 0:
            # cur = stack[-1]
            while cur.left and (not (cur.left in visited)):
                cur = cur.left
                stack.append(cur)
            v = stack.pop(-1)
            orders.append(v.val)
            visited.append(v)
            if v.right:
                cur = v.right
                stack.append(cur)
            else:
                if len(stack) > 0:
                    cur = stack[-1]

        return orders


# recrusion version
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         if root is None:
#             return []
#         if root.left is None and root.right is None:
#             return [root.val]
#         order_left = self.inorderTraversal(root.left)
#         order_right = self.inorderTraversal(root.right)
#         return_order = order_left + [root.val]
#         return_order += order_right
#         return return_order

# if __name__ == "__main__":
