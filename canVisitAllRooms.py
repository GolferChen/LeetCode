from typing import List
from collections import deque

# Official Solution
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = deque([0])
        # visited = deque([0])
        visited = [False] * len(rooms)
        visited[0] = True
        while len(stack) > 0:
            current = stack.pop()
            for j in rooms[current]:
                # if not (j in visited):
                if not visited[j]:
                    # visited.append(j)
                    visited[j] = True
                    stack.append(j)
        # return len(visited) == len(rooms)
        return all(visited)

# Self Version
# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         can_visited = deque()
#         def dfs(cur, target):
#             stack = deque([cur])
#             visited = deque([cur])
#             while len(stack) > 0:
#                 current = stack.pop()
#                 can_visited.append(current)
#                 if current == target:
#                     return True
#                 for j in rooms[current]:
#                     if not (j in visited):
#                         visited.append(j)
#                         stack.append(j)
#             return False
#         for i in range(1, len(rooms)):
#             if i in can_visited:
#                 continue
#             reach_flag = dfs(0, i)
#             if not reach_flag:
#                 return False
#         return True

if __name__ == "__main__":
    rooms = [[1],[2],[3],[]]
    # rooms = [[1, 3], [3, 0, 1], [2], [0]]
    solution = Solution()
    res = solution.canVisitAllRooms(rooms)
    print(res)
