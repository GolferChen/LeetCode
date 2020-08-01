//
// Created by Golfer on 2020/8/1.
//
#include <vector>
#include <cstdio>
#include <stack>
using namespace std;

class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        stack<int> s;
        s.push(0);
        vector<bool> visited(rooms.size(), false);
        visited[0] = true;
        while (! s.empty()) {
            int current = s.top();
            s.pop();
            for (int & j : rooms[current]) {
                if (! visited[j]) {
                    visited[j] = true;
                    s.push(j);
                }
            }
        }
        for (_Bit_reference v : visited) {
            if (! v)
                return false;
        }
        return true;
    }
};
