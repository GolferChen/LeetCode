//
// Created by Golfer on 2020/7/19.
//

#include <cstdio>
#include <queue>
#include <vector>
#include <set>
#include <cmath>

using namespace std;


//class Solution {
//public:
//    int numIslands(vector<vector<char>>& grid) {
//        int n = grid.size();
//        int m = grid[0].size();
//        int first_land;
//        for (int i = 0; i < n; i ++) {
//            for (int j = 0; j < m; j++) {
//                if (grid[i][j] == '1') {
//                    first_land = i * m + j;
//                    i = n; // break
//                    j = m; // break
//                }
//            }
//        }
//        queue<int> q;
////        q.push(0);
//        q.push(first_land);
//        set<int> visited;
////        visited.insert(0);
//        visited.insert(first_land);
//        int n_lands = 0;
//        int row_shift[] = {1, -1, 0, 0};
//        int col_shift[] = {0, 0, 1, -1};
//        int n_shift = 4;
//        while (! q.empty()) {
//            int current_position = q.front();
//            q.pop();
//            int * current_position_2d = get_index(current_position, n, m);
//            int row = current_position_2d[0];
//            int col = current_position_2d[1];
//            char current = grid[row][col];
//            if (current == '0') {
//                continue;
//            }
//            int cnt = 0;
//            for (int i = 0; i < n_shift; i++) {
//                int child_row = row + row_shift[i];
//                int child_col = col + col_shift[i];
//                if (child_row < 0 || child_col < 0) {
//                    ++cnt;
//                    continue;
//                }
//                int child_position = child_row * m + child_col;
//                if (visited.find(child_position) != visited.end() || grid[child_row][child_col] == '0') {
//                    ++cnt;
//                }
//                else {
//                    q.push(child_position);
//                    visited.insert(child_position);
//                }
//            }
//            if (cnt == 4) {
//                ++n_lands;
//            }
//
//        }
//        return n_lands;
//    }
//
//    int * get_index(int position, int n, int m) {
//        int * position_2d = new int[2];
//        position_2d[0] = floor(position / m);
//        position_2d[1] = (position - position_2d[0] * m);
//        return position_2d;
//    }
//
//    bool is_water(vector<vector<char>>& grid, int row, int col) {
//        if (row >=0 && col >= 0) {
//            return grid[row][col] == '0';
//        }
//        return true;
//    }
//};


class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
//        int m = grid[0].size();
        int n_lands = 0;
        for (int i = 0; i < n; i++) {
            int m = grid[i].size(); // different rows may have different cols
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    int position = i * m + j;
                    bfs(position, grid, n, m);
                    ++n_lands;
                }
            }
        }

        return n_lands;
    }

    void bfs(int position, vector<vector<char>>& grid, int n, int m) {
        queue<int> q;
        q.push(position);
        set<int> visited;
        visited.insert(position);
        int row_shift[] = {1, -1, 0, 0};
        int col_shift[] = {0, 0, 1, -1};
        int n_shift = 4;
        while (! q.empty()) {
            int current_position = q.front();
            q.pop();
            int * current_position_2d = get_index(current_position, n, m);
            int row = current_position_2d[0];
            int col = current_position_2d[1];
            if (row >= 0 && row < n && col >= 0 && col < m && grid[row][col] == '1') {
                grid[row][col] = '0';
            }
            for (int i = 0; i < n_shift; i++) {
                int child_row = row + row_shift[i];
                int child_col = col + col_shift[i];
                if (child_row < 0 || child_row >= n || child_col < 0 || child_col >= m) {
                    continue;
                }
                int child_position = child_row * m + child_col;
                if (visited.find(child_position) == visited.end() && grid[child_row][child_col] == '1') {
                    q.push(child_position);
                    visited.insert(child_position);
                }
            }
        }
    }

    int * get_index(int position, int n, int m) {
        int * position_2d = new int[2];
        position_2d[0] = floor(position / m);
        position_2d[1] = (position - position_2d[0] * m);
        return position_2d;
    }

};

int main() {
    vector<vector<char>> grid = {{'1','1','0','0','0'},
                                 {'1','1','0','0','0'},
                                 {'0','0','1','0','0'},
                                 {'0','0','0','1','1'}};
    Solution solution = Solution();
    int n_lands = solution.numIslands(grid);
    printf("%d", n_lands);
}