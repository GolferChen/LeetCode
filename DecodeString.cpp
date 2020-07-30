//
// Created by Golfer on 2020/7/28.
//

#include <string>
#include <stack>
using namespace std;
#include <cstdio>
#include <iostream>

// Version 1, Stack
//class Solution {
//public:
//    string decodeString(string s) {
//        stack<string> stack_string;
//        stack<int> stack_num;
//        int number = 0;
//        string result= "";
//        for (char &c : s) {
////            if ('0' <= c <= '9') { // wrong !!!
////                number = number * 10 + c - '0';
////            }
//            if ('0' <= c && c <= '9') {
//                number = number * 10 + c - '0';
//            }
//            else if (c == '[') {
//                stack_num.push(number);
//                number = 0;
//                stack_string.push(result);
//                result = "";
//            }
//            else if (c == ']') {
//                int num = stack_num.top();
//                stack_num.pop();
//                string last_string = stack_string.top();
//                stack_string.pop();
//                string result_tmp = result;
//                for (int i = 0; i < num - 1; i++) {
//                    result += result_tmp;
//                }
//                result = last_string + result;
////                result = last_string + result
//            }
//            else {
//                result += c;
//            }
//        }
//        return result;
//    }
//};

// Version 2, recrusive
class Solution {
public:
    string decodeString(string s) {
        return dfs(s, 0).second;
    }
    pair<int, string> dfs(string s, int i) {
        int number = 0;
        string result = "";
        while (i < s.size()) {
            char c = s[i];
            if (c >= '0' && c <= '9') {
                number = number * 10 + c - '0';
            }
            else if (c == '[') {
                pair<int, string> dfs_call = dfs(s, i + 1);
                i = dfs_call.first;
                string tmp = dfs_call.second;
                for (int j = 0; j < number; j++)
                    result += tmp;
                number = 0;
            }
            else if (c == ']') {
                return make_pair(i, result);
            }
            else {
                result += c;
            }
            ++i;
        }
        return make_pair(-1, result);
    }
};

int main() {
    string s = "3[a]2[bc]";
    Solution solution = Solution();
    string decode_s = solution.decodeString(s);
    cout << decode_s << endl;
    return 0;
}

