from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = [(sr, sc)]
        # image[sr][sc] = newColor // we should color (sr, sc) at last
        visited = [(sr, sc)]
        row_shift = [-1, 1, 0, 0]
        col_shift = [0, 0, -1, 1]
        while len(queue) > 0:
            current_row, current_col = queue.pop(0)
            for i, j in zip(row_shift, col_shift):
                neighbor_row = current_row + i
                neighbor_col = current_col + j
                if neighbor_row < 0 or neighbor_row >= len(image) or neighbor_col < 0 or neighbor_col >= len(image[neighbor_row]):
                    continue
                if (not ((neighbor_row, neighbor_col) in visited)) and image[neighbor_row][neighbor_col] == image[sr][sc]:
                    image[neighbor_row][neighbor_col] = newColor
                    visited.append((neighbor_row, neighbor_col))
                    queue.append((neighbor_row, neighbor_col))
        image[sr][sc] = newColor
        return image

if __name__ == "__main__":
    solution = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    new_image = solution.floodFill(image, 1, 1, 2)
    print(new_image)

