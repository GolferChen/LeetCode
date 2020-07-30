//
// Created by Golfer on 2020/7/20.
//

#include <stack>
using namespace std;


class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> s_data;
    stack<int> s_min;

    MinStack() {
    }

    void push(int x) {
        s_data.push(x);
        if (s_min.empty()) {
            s_min.push(x);
        }
        else {
            if (x < s_min.top()) {
                s_min.push(x);
            }
            else {
                s_min.push(s_min.top());
            }
        }
    }

    void pop() {
        if (s_data.empty()) {
            return;
        }
        s_data.pop();
        s_min.pop();
    }

    int top() {
//        if (s_data.empty()) {
//            return;
//        }
        return s_data.top();
    }

    int getMin() {
        return s_min.top();
    }
};

/**
 * Your stack_minStack object will be instantiated and called as such:
 * stack_minStack* obj = new stack_minStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getstack_min();
 */

