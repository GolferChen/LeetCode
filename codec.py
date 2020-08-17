from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # if root is None:
        #     return str([])
        # orders = [root.val]
        orders = []
        queue = [root]
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur:
                orders.append(cur.val)
                # if cur.left:
                #     queue.append(cur.left)
                # else:
                #     queue.append(None)
                # if cur.right:
                #     queue.append(cur.right)
                # else:
                #     queue.append(None)
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                orders.append(None)
                # orders.append('#')
        return str(orders)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # if data == "[]":
        #     return None
        data = data[1:-1].replace(" ", "").split(",")
        for index, item in enumerate(data):
            if item != "None":
                data[index] = int(item)
            else:
                data[index] = None
        if data[0] is None:
            return None
        root = TreeNode(data[0])
        parent = root
        parents = []
        is_left = True
        for item in data[1:]:
            if not (item is None):
                if is_left:
                    new_node = TreeNode(item)
                    parent.left = new_node
                    parents.append(new_node)
                else:
                    new_node = TreeNode(item)
                    parent.right = new_node
                    parents.append(new_node)
            if not is_left:
                if len(parents) > 0:
                    parent = parents.pop(0)
            is_left = (not is_left)
        return root







# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))