//
// Created by Golfer on 2020/7/21.
//

#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> my_stack;
        int n = s.size();
        if (n == 0)
            return true;
        for (char & c : s) {
            if (my_stack.empty())
                my_stack.push(c);
            else {
                bool match_flag = is_match(my_stack.top(), c);
                if (match_flag)
                    my_stack.pop();
                else
                    my_stack.push(c);
            }
        }
        return my_stack.empty();
    }

    bool is_match(char a, char b) {
        if (a == '(')
            return b == ')';
        if (a == '[')
            return b == ']';
        if (a == '{')
            return b == '}';
        return false;
    }
};

int main() {
    string s = "()";
    Solution solution = Solution();
    bool valid = solution.isValid(s);
    printf("%d", valid);
}

