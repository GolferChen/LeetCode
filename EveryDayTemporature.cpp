//
// Created by Golfer on 2020/7/21.
//

#include <vector>
using namespace std;
#include <cstdio>
#include <stack>
#include <iostream>

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int n = T.size();
        vector<int> days;
        days.resize(n);
        for (int i = 0; i < n; i++) {
            days[i] = 0;
        }
        stack<int> s;
        for (int index = n - 1; index >= 0; index--) {
            int t = T[index];
            while (s.size() != 0 && t >= T[s.top()]) {
                s.pop();
            }
            if (s.size() != 0) {
                days[index] = s.top() - index;
            }
            s.push(index);
        }
        return days;
    }
};

int main () {
    vector<int> T = {73,74,75,71,69,72,76,73};
    Solution solution = Solution();
    vector<int> days = solution.dailyTemperatures(T);
}