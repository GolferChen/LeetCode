from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque([(0, root)])
        output = []
        while len(queue) > 0:
            cur_level, cur = queue.popleft()
            if cur:
                if len(output) <= cur_level: # or len(output) == cur_level:
                    output.append([cur.val])
                else:
                    output[cur_level].append(cur.val)
                if cur.left:
                    queue.append((cur_level+1, cur.left))
                if cur.right:
                    queue.append((cur_level+1, cur.right))
        return output

