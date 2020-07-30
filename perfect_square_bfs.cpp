//
// Created by Golfer on 2020/7/19.
//


#include <iostream>
#include <queue>
#include <vector>
using namespace std;


class Solution {
public:
    inline int numSquares(int n) {
        queue <int> q;
        q.push(n);
        int *visited = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            visited[i] = 0;
        }
        vector<int> numbers;
        for (int i = 1; i * i <= n; i++) {
            numbers.push_back(i * i);
        }
        int n_levels = 0;
        while (!q.empty()) {
            ++n_levels;
            int qLen = q.size();
            for (int i = 0; i < qLen; ++i){
                int current_num = q.front();
                q.pop();
                for (int j = 0; j < numbers.size(); j++) {
                    int child = current_num - numbers[j];
                    if (child == 0) {
                        return n_levels;
                    }
                    if (child > 0) {
                        if (!visited[child]) {
                            q.push(child);
                        }
                        else {
                            visited[i] = 1;
                        }
                    }
                }
            }
        }
        return 0;
    }
};

int main() {
    Solution s = Solution();
    int n = 13;
    cout << s.numSquares(n) << endl;
    return 0;
}
