//
// Created by Golfer on 2020/7/29.
//

#include <vector>
#include <cstdio>
#include <queue>
#include <set>
using namespace std;

class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        queue<pair<int, int>> q;
        pair<int, int> pair_sr_sc = make_pair(sr, sc);
        q.push(pair_sr_sc);
        set<pair<int, int>> visited;
        visited.insert(pair_sr_sc);
        vector<int> row_shift = {-1, 1, 0, 0};
        vector<int> col_shift = {0, 0, -1, 1};
        while (! q.empty()) {
            pair<int, int> current = q.front();
            int current_row = current.first;
            int current_col = current.second;
            q.pop();
            for (int i = 0; i < row_shift.size(); i++) {
                int neighbor_row = current_row + row_shift[i];
                int neighbor_col = current_col + col_shift[i];
                if (neighbor_row < 0 || neighbor_row >= image.size() || neighbor_col < 0 || neighbor_col >= image[neighbor_row].size()) {
                    continue;
                }
                pair<int, int> pair_neighbor = make_pair(neighbor_row, neighbor_col);
                if (image[neighbor_row][neighbor_col] == image[sr][sc] && visited.find(pair_neighbor) == visited.end()) {
                    image[neighbor_row][neighbor_col] = newColor;
                    visited.insert(pair_neighbor);
                    q.push(pair_neighbor);
                }
            }
        }
        image[sr][sc] = newColor;
        return image;
    }
};

