from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        update_matrix = [[-1 for j in range(len(matrix[i]))] for i in range(len(matrix))]

        def dfs(i, j):
            if update_matrix[i][j] != -1:
                return update_matrix[i][j]
            if matrix[i][j] == 0:
                update_matrix[i][j] = 0
                return update_matrix[i][j]
            # min_value = 10000 + 1
            neighbor_values = []
            for m, n in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                neighbor_i = i + m
                neighbor_j = j + n
                if neighbor_i < 0 or neighbor_i >= len(matrix) or neighbor_j < 0 or neighbor_j >= len(
                        matrix[neighbor_i]):
                    continue
                # neighbor_value = dfs(neighbor_i, neighbor_j) if update_matrix[neighbor_i][neighbor_j] == -1 else \
                #     update_matrix[neighbor_i][neighbor_j]
                neighbor_value = dfs(neighbor_i, neighbor_j)
                neighbor_values.append(neighbor_value + 1)
                if neighbor_value == 0:
                    break
            update_matrix[i][j] = min(neighbor_values)
            return update_matrix[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if update_matrix[i][j] == -1:
                    dfs(i, j)
        return update_matrix


if __name__ == "__main__":
    matrix = [[0, 0, 0],
              [0, 1, 0],
              [1, 1, 1]]
    solution = Solution()
    update_matrix = solution.updateMatrix(matrix)
    print(update_matrix),
