from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Self, Wrong
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
#         def build(val, post_index, parent_inorder_index):
#             if not (val in self.map.keys()):
#                 self.map[val] = TreeNode(val)
#             inorder_index = inorder.index(val)
#             # left_cnt = inorder_index - parent_inorder_index - 1
#             # right_cnt = len(inorder) - 1 - inorder_index
#             if inorder_index > parent_inorder_index:
#                 left_cnt = inorder_index - parent_inorder_index - 1
#                 right_cnt = len(inorder) - 1 - inorder_index
#             else:
#                 right_cnt = parent_inorder_index - inorder_index - 1
#                 left_cnt = inorder_index
#             if left_cnt != 0 and (post_index-left_cnt-right_cnt) >= 0 and (post_index-left_cnt-right_cnt) < len(postorder):
#                 left_root_val = postorder[post_index-left_cnt-right_cnt]
#                 self.map[left_root_val] = TreeNode(left_root_val)
#                 self.map[val].left = self.map[left_root_val]
#                 build(left_root_val, post_index-left_cnt-right_cnt, inorder_index)
#             if right_cnt != 0 and (post_index-1) >= 0 and (post_index-1) < len(postorder):
#                 right_root_val = postorder[post_index-1]
#                 self.map[right_root_val] = TreeNode(right_root_val)
#                 self.map[val].right = self.map[right_root_val]
#                 build(right_root_val, post_index-1, inorder_index)
#         if len(postorder) == 0:
#             return None
#         self.map = {}
#         build(postorder[-1], len(postorder)-1, -1)
#         return self.map[postorder[-1]]


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            root_val = postorder.pop(-1)
            root_index = val_index_map[root_val]
            root = TreeNode(root_val)
            root.right = helper(root_index+1, right) # must right first
            root.left = helper(left, root_index-1)
            return root

        val_index_map = {val: index for index, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)



if __name__ == "__main__":
    post = [3, 2, 1]
    inorder = [3, 2, 1]
    solution = Solution()
    t = solution.buildTree(inorder, post)
    print(t.val)

