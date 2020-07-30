//
// Created by Golfer on 2020/7/19.
//

#include <cstdio>
#include <queue>
#include <string>
#include <set>

using namespace std;

class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        // change vector to set for quick query
        set<string> deads;
        for (string &item : deadends) {
            deads.insert(item);
        }
        string init = "0000";
        if (deads.find(init) != deads.end()) {
            return -1;
        }
        if (target == init) {
            return 0;
        }
        // visited
        set<string> visited;
        visited.insert(init);
        queue<string> q;
        q.push(init);
        int n_turns = 0;
        while (! q.empty()) {
            ++n_turns;
            int q_size = q.size();
            for (int i = 0; i < q_size; i ++) {
                string current = q.front();
                q.pop();
                for (int j = 0; j < 4; j++) {
                    string child_plus_one = get_child_plus_one(current, j);
                    if (child_plus_one == target) {
                        return n_turns;
                    }
                    if (deads.find(child_plus_one) == deads.end() && visited.find(child_plus_one) == visited.end()) {
                        q.push(child_plus_one);
                        visited.insert(child_plus_one);
                    }
                    string child_minus_one = get_child_minus_one(current, j);
                    if (child_minus_one == target) {
                        return n_turns;
                    }
                    if (deads.find(child_minus_one) == deads.end() && visited.find(child_minus_one) == visited.end()) {
                        q.push(child_minus_one);
                        visited.insert(child_minus_one);
                    }
                }
            }
        }
        return -1;
    }

    string get_child_plus_one(string current, int position) {
        if (current[position] == '9') {
            current[position] = '0';
        }
        else {
            current[position] += 1;
        }
        return current;
    }

    string get_child_minus_one(string current, int position) {
        if (current[position] == '0') {
            current[position] = '9';
        }
        else {
            current[position] -= 1;
        }
        return current;
    }
};


int main() {

    vector<string> deadends = {"0201", "0101", "0102", "1212", "2002"};
    string target = "0202";
    Solution solution = Solution();
    int n_turns = solution.openLock(deadends, target);
    printf("%d", n_turns);
}

