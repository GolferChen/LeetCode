from typing import List
from collections import deque

# DP Version, bottom up
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        update_matrix = [[10000 + 1 for j in range(len(matrix[i]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    update_matrix[i][j] = 0
        for i in range(len(matrix)): # up, left
            for j in range(len(matrix[i])):
                if update_matrix[i][j] == 0:
                    continue
                if i - 1 >= 0:
                    update_matrix[i][j] = min(update_matrix[i][j], 1 + update_matrix[i-1][j])
                if j - 1 >= 0:
                    update_matrix[i][j] = min(update_matrix[i][j], 1 + update_matrix[i][j-1])
        for i in range(len(matrix) - 1, -1, -1): # down, left
            for j in range(len(matrix[i])):
                if update_matrix[i][j] == 0:
                    continue
                if i + 1 < len(matrix):
                    update_matrix[i][j] = min(update_matrix[i][j], 1 + update_matrix[i+1][j])
                if j - 1 >= 0:
                    update_matrix[i][j] = min(update_matrix[i][j], 1 + update_matrix[i][j-1])
        for i in range(len(matrix)): # up, right
            for j in range(len(matrix[i]) - 1, -1, -1):
                if update_matrix[i][j] == 0:
                    continue
                if i - 1 >= 0:
                    update_matrix[i][j] = min(update_matrix[i][j], 1 + update_matrix[i-1][j])
                if j + 1 < len(matrix[i]):
                    update_matrix[i][j] = min(update_matrix[i][j], 1 + update_matrix[i][j+1])
        for i in range(len(matrix) - 1, -1, -1): # down, right
            for j in range(len(matrix[i]) - 1, -1, -1):
                if update_matrix[i][j] == 0:
                    continue
                if i + 1 < len(matrix):
                    update_matrix[i][j] = min(update_matrix[i][j], 1 + update_matrix[i+1][j])
                if j + 1 < len(matrix[i]):
                    update_matrix[i][j] = min(update_matrix[i][j], 1 + update_matrix[i][j+1])
        return update_matrix



# BFS
# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         # queue = []
#         update_matrix = [[-1 for j in range(len(matrix[i]))] for i in range(len(matrix))]
#         zero_index = []
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if matrix[i][j] == 0:
#                     # queue.append((i, j))
#                     zero_index.append((i, j))
#                     update_matrix[i][j] = 0
#         queue = deque(zero_index)
#         while len(queue) > 0:
#             # current_row, current_col = queue.pop(0)
#             current_row, current_col = queue.popleft()
#             for m, n in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
#                 neighbor_row = current_row + m
#                 neighbor_col = current_col + n
#                 if neighbor_row < 0 or neighbor_row >= len(matrix) or neighbor_col < 0 or neighbor_col >= len(
#                         matrix[neighbor_row]):
#                     continue
#                 if update_matrix[neighbor_row][neighbor_col] == -1:
#                     queue.append((neighbor_row, neighbor_col))
#                     update_matrix[neighbor_row][neighbor_col] = update_matrix[current_row][current_col] + 1
#         return update_matrix


# DFS, Wrong, TLE, recrusion depth exceeds
# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         update_matrix = [[-1 for j in range(len(matrix[i]))] for i in range(len(matrix))]
#
#         def dfs(i, j):
#             if update_matrix[i][j] != -1:
#                 return update_matrix[i][j]
#             if matrix[i][j] == 0:
#                 update_matrix[i][j] = 0
#                 return update_matrix[i][j]
#             # min_value = 10000 + 1
#             neighbor_values = []
#             for m, n in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
#                 neighbor_i = i + m
#                 neighbor_j = j + n
#                 if neighbor_i < 0 or neighbor_i >= len(matrix) or neighbor_j < 0 or neighbor_j >= len(
#                         matrix[neighbor_i]):
#                     continue
#                 # neighbor_value = dfs(neighbor_i, neighbor_j) if update_matrix[neighbor_i][neighbor_j] == -1 else \
#                 #     update_matrix[neighbor_i][neighbor_j]
#                 neighbor_value = dfs(neighbor_i, neighbor_j)
#                 neighbor_values.append(neighbor_value + 1)
#                 if neighbor_value == 0:
#                     break
#             update_matrix[i][j] = min(neighbor_values)
#             return update_matrix[i][j]
#
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if update_matrix[i][j] == -1:
#                     dfs(i, j)
#         return update_matrix


if __name__ == "__main__":
    matrix = [[0, 0, 0],
              [0, 1, 0],
              [1, 1, 1]]
    solution = Solution()
    update_matrix = solution.updateMatrix(matrix)
    print(update_matrix),
