from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            root_val = preorder.pop(0)
            root_index = val_index_map[root_val]
            root = TreeNode(root_val)
            root.left = helper(left, root_index-1) # must first first
            root.right = helper(root_index+1, right)
            return root

        val_index_map = {val: index for index, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)
