from typing import List


# BFS Version
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#
#         def bfs(root_row, root_col):
#             n_rows = len(grid)
#             q = [(root_row, root_col)]
#             visited = [(root_row, root_col)]
#             row_shift = [-1, 1, 0, 0]
#             col_shift = [0, 0, -1, 1]
#             n_shift = len(row_shift)
#             while len(q) != 0:
#                 row, col = q.pop(0)
#                 # if 0 <= row < n_rows and 0 <= col < n_cols and grid[row][col] == '1':
#                 #     grid[row][col] = '0'
#                 if 0 <= row < n_rows and 0 <= col < len(grid[row]) and grid[row][col] == '1':
#                     grid[row][col] = '0'
#                 for k in range(n_shift):
#                     child_row = row + row_shift[k]
#                     child_col = col + col_shift[k]
#                     # if child_row < 0 or child_row >= n_rows or child_col <= 0 or child_col >= n_cols:
#                     #     continue
#                     if child_row < 0 or child_row >= n_rows or child_col < 0 or child_col >= len(grid[child_row]):
#                         continue
#                     if grid[child_row][child_col] == '1' and (not (child_row, child_col) in visited):
#                         visited.append((child_row, child_col))
#                         q.append((child_row, child_col))
#
#         n_lands = 0
#         n = len(grid)
#         for i in range(n):
#             m = len(grid[i])
#             for j in range(m):
#                 if grid[i][j] == '1':
#                     bfs(i, j)
#                     n_lands += 1
#         return n_lands

# DFS Version
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = []
        def dfs(row, col):
            n_rows = len(grid)
            visit(row, col)
            # visited = [(row, col)] // wrong for recrusive !!!
            visited.append((row, col))
            row_shift = [-1, 1, 0, 0]
            col_shift = [0, 0, -1, 1]
            n_shift = len(row_shift)
            for k in range(n_shift):
                child_row = row + row_shift[k]
                child_col = col + col_shift[k]
                if child_row < 0 or child_row >= n_rows or child_col < 0 or child_col >= len(grid[child_row]):
                    continue
                if grid[child_row][child_col] == '1' and (not ((child_row, child_col) in visited)):
                    dfs(child_row, child_col)
                    # visited.append((child_row, child_col))

        def visit(row, col):
            n_rows = len(grid)
            if 0 <= row < n_rows and 0 <= col < len(grid[row]) and grid[row][col] == '1':
                grid[row][col] = '0'

        n_lands = 0
        n = len(grid)
        for i in range(n):
            m = len(grid[i])
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    n_lands += 1
        return n_lands


if __name__ == "__main__":
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    s = Solution()
    n_lands = s.numIslands(grid)
    print("%d" % n_lands)
