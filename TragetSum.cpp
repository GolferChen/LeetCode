//
// Created by Golfer on 2020/7/25.
//

#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        vector<unordered_map<int, int>> memory(nums.size());
        int count = dfs(0, 0, nums, S, memory);
        return count;
    }

    int dfs(int current_sum, int index, vector<int>& nums, int S, vector<unordered_map<int, int>>& memory) {
        if (index == nums.size()) {
            return (int)(current_sum == S);
        }
        if (memory[index].count(current_sum)) {
            return memory[index][current_sum];
        }
        int cnt_left = dfs(current_sum + nums[index], index + 1, nums, S, memory);
        int cnt_right = dfs(current_sum - nums[index], index + 1, nums, S, memory);
        memory[index][current_sum] = cnt_left + cnt_right;
        return memory[index][current_sum];
    }
};

//class Solution {
//public:
//    int findTargetSumWays(vector<int>& nums, int S) {
//        int count = dfs(0, 0, nums, S);
//        return count;
//    }
//
//    int dfs(int current_sum, int index, vector<int>& nums, int S) {
//        if (index == nums.size()) {
//            return (int)(current_sum == S);
//        }
//        int cnt_left = dfs(current_sum + nums[index], index + 1, nums, S);
//        int cnt_right = dfs(current_sum - nums[index], index + 1, nums, S);
//        return cnt_left + cnt_right;
//    }
//};

//class Solution {
//public:
//    map<vector<int>, int> memory;
//    int findTargetSumWays(vector<int>& nums, int S) {
//        int count = dfs(0, 0, nums, S);
//        return count;
//    }
//
//    int dfs(int current_sum, int index, vector<int>& nums, int S) {
//        if (index == nums.size()) {
//            return (int)(current_sum == S);
//        }
//        vector<int> id;
//        id.push_back(current_sum);
//        id.push_back(index);
//        if (memory.find(id) != memory.end()) {
//            return memory[id];
//        }
//        else {
//            int cnt_left = dfs(current_sum + nums[index], index + 1, nums, S);
//            int cnt_right = dfs(current_sum - nums[index], index + 1, nums, S);
//            memory[id] = cnt_left + cnt_right;
//            return memory[id];
//        }
//    }
//};
