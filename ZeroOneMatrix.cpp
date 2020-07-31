//
// Created by Golfer on 2020/8/1.
//

#include <vector>
#include <queue>
//#include <set>
#include <cstdio>
using namespace std;

// BFS Version
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        queue<pair<int, int>> q;
//        vector<vector<int>> update_matrix(matrix.size(), vector<int>(matrix[0].size(), -1));
        vector<vector<int>> update_matrix;
        update_matrix.resize(matrix.size());
        for (int i = 0; i < matrix.size(); i++) {
            update_matrix[i].resize(matrix[i].size());
            for (int j = 0; j < matrix[i].size(); j++) {
                if (matrix[i][j] == 0) {
                    q.push(make_pair(i, j));
                    update_matrix[i][j] = 0;
                }
                else
                    update_matrix[i][j] = -1;
            }
        }
        vector<int> row_shift = {-1, 1, 0, 0};
        vector<int> col_shift = {0, 0, -1, 1};
        while (! q.empty()) {
            pair<int, int> current = q.front();
            q.pop();
            int current_row = current.first;
            int current_col = current.second;
            for (int i = 0; i < row_shift.size(); i++) {
                int neighbor_row = current_row + row_shift[i];
                int neighbor_col = current_col + col_shift[i];
                if (neighbor_row < 0 || neighbor_row >= matrix.size() || neighbor_col < 0 || neighbor_col >= matrix[neighbor_row].size())
                    continue;
                if (update_matrix[neighbor_row][neighbor_col] == -1) {
                    update_matrix[neighbor_row][neighbor_col] = update_matrix[current_row][current_col] + 1;
                    q.push(make_pair(neighbor_row, neighbor_col));
                }
            }
        }
        return update_matrix;
    }
};

// DFS Version,
// AddressSanitizer: stack-overflow
//#define inf 10000 + 1
//
//class Solution {
//public:
//    vector<vector<int>> update_matrix;
//    vector<int> row_shift = {-1, 1, 0, 0};
//    vector<int> col_shift = {0, 0, -1, 1};
//    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
//        update_matrix.resize(matrix.size());
//        for (int i = 0; i < matrix.size(); i++) {
//            update_matrix[i].resize(matrix[i].size());
//            for (int j = 0; j < matrix[i].size(); j++) {
//                update_matrix[i][j] = inf;
//            }
//        }
//        for (int i = 0; i < matrix.size(); i++) {
//            for (int j = 0; j < matrix[i].size(); j++) {
//                if (update_matrix[i][j] == inf) {
//                    dfs(matrix, i, j);
//                }
//            }
//        }
//        return update_matrix;
//    }
//    int dfs(vector<vector<int>>& matrix, int row, int col) {
//        if (update_matrix[row][col] != inf)
//            return update_matrix[row][col];
//        if (matrix[row][col] == 0) {
//            update_matrix[row][col] = 0;
//            return update_matrix[row][col];
//        }
//        for (int i = 0; i < row_shift.size(); i++) {
//            int nei_row = row + row_shift[i];
//            int nei_col = col + col_shift[i];
//            if (nei_row < 0 || nei_row >= matrix.size() || nei_col < 0 || nei_col >= matrix[nei_row].size())
//                continue;
//            update_matrix[row][col] = min(update_matrix[row][col], dfs(matrix, nei_row, nei_col) + 1);
//        }
//        return update_matrix[row][col];
//    }
//};

//int main() {
//
//}

