
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

# # Correct, DFS Version
# class Solution:
#     def __init__(self):
#         self.map = dict()
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node: # deal with empty graph
#             return node
#         node_clone = Node(val=node.val)
#         # self.visited.append(node.val)
#         self.map[node] = node_clone
#         for neighbor in node.neighbors:
#             # if not (neighbor.val in self.visited):
#             if not (neighbor in self.map.keys()):
#                 neighbor_clone = self.cloneGraph(neighbor)
#                 node_clone.neighbors.append(neighbor_clone)
#             else:
#                 node_clone.neighbors.append(self.map[neighbor])
#                 # node_clone.neighbors.append(neighbor)
#         return node_clone

# Correct, BFS Version
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: # deal with empty graph
            return node
        node_clone = Node(val=node.val)
        # map = dict()
        map = {node: node_clone}
        queue = [node]
        # queue.append(node)
        # parent = dict()
        while len(queue) > 0:
            # queue_size = len(queue)
            # for i in range(queue_size):
            current_node = queue.pop(0)
            # clone_node = Node(val=current_node.val)
            # map[current_node] = clone_node
            for neighbor in current_node.neighbors:
                if not (neighbor in map.keys()):
                    neighbor_clone = Node(val=neighbor.val)
                    map[neighbor] = neighbor_clone
                    queue.append(neighbor)
                    map[current_node].neighbors.append(neighbor_clone)
                    # parent[neighbor] = clone_node
                else:
                    map[current_node].neighbors.append(map[neighbor])
        # for child_ori in list(parent.keys()):
        #     parent_clone = parent[child_ori]
        #     parent_clone.neighbors.append(map[child_ori])

        return node_clone


    ## Wrong
# class Solution:
#     def __init__(self):
#         self.visited = []
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         node_clone = Node(val=node.val)
#         self.visited.append(node.val)
#         for neighbor in node.neighbors:
#             if not (neighbor.val in self.visited):
#                 neighbor_clone = self.cloneGraph(neighbor)
#                 node_clone.neighbors.append(neighbor_clone)
#             else:
#                 node_clone.neighbors.append(neighbor)
#         return node_clone

