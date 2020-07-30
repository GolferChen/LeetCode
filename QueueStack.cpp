//
// Created by Golfer on 2020/7/27.
//

#include <queue>
using namespace std;
#include <cstdio>

//// Version 1
//class MyStack {
//public:
//    queue<int> q;
//    queue<int> q_help;
//    /** Initialize your data structure here. */
//    MyStack() {
//    }
//
//    /** Push element x onto stack. */
//    void push(int x) {
//        q.push(x);
//    }
//
//    /** Removes the element on top of the stack and returns that element. */
//    int pop() {
//        int q_size = q.size();
//        for (int i = 0; i < q_size - 1; i++) {
//            int front = q.front();
//            q.pop();
//            q_help.push(front);
//        }
//        int back = q.front();
//        q.pop();
//        while (! q_help.empty()) {
//            int front = q_help.front();
//            q_help.pop();
//            q.push(front);
//        }
//        return back;
//    }
//
//    /** Get the top element. */
//    int top() {
//        int q_size = q.size();
//        for (int i = 0; i < q_size - 1; i++) {
//            int front = q.front();
//            q.pop();
//            q_help.push(front);
//        }
//        int back = q.front();
//        q.pop();
//        q_help.push(back);
//        while (! q_help.empty()) {
//            int front = q_help.front();
//            q_help.pop();
//            q.push(front);
//        }
//        return back;
//    }
//
//    /** Returns whether the stack is empty. */
//    bool empty() {
//        return q.empty();
//    }
//};

//// Version 2, two queue
//class MyStack {
//public:
//    queue<int> q;
//    queue<int> q_help;
//    /** Initialize your data structure here. */
//    MyStack() {
//    }
//
//    /** Push element x onto stack. */
//    void push(int x) {
//        if (! q.empty()) {
//            q.push(x);
//        }
//        else {
//            q_help.push(x);
//        }
//    }
//
//    /** Removes the element on top of the stack and returns that element. */
//    int pop() {
////        if (q.empty() && q_help.empty()) {
////        }
//        queue<int> *src;
//        queue<int> *des;
//        if (! q.empty()) {
//            src = &q;
//            des = &q_help;
//        }
//        else {
//            src = &q_help;
//            des = &q;
//        }
//        int size = src->size();
//        for (int i = 0; i < size - 1; i++) {
//            int front = src->front();
//            src->pop();
//            des->push(front);
//        }
//        int back = src->front();
//        src->pop();
//        return back;
//    }
//
//    /** Get the top element. */
//    int top() {
//        //        if (q.empty() && q_help.empty()) {
////        }
//        queue<int> *src;
//        queue<int> *des;
//        if (! q.empty()) {
//            src = &q;
//            des = &q_help;
//        }
//        else {
//            src = &q_help;
//            des = &q;
//        }
//        int size = src->size();
//        for (int i = 0; i < size - 1; i++) {
//            int front = src->front();
//            src->pop();
//            des->push(front);
//        }
//        int back = src->front();
//        src->pop();
//        des->push(back);
//        return back;
//    }
//
//    /** Returns whether the stack is empty. */
//    bool empty() {
//        return (q.empty() && q_help.empty());
//    }
//};

// Version 3, one queue
class MyStack {
public:
    queue<int> q;
    /** Initialize your data structure here. */
    MyStack() {
    }

    /** Push element x onto stack. */
    void push(int x) {
        q.push(x);
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop() {
//        int size = q.size();
//        for (int i = 0; i < size - 1; i ++) {
        for (int i = 0; i < q.size() - 1; i ++) {
            int front = q.front();
            q.pop();
            q.push(front);
        }
        int back = q.front();
        q.pop();
        return back;
    }

    /** Get the top element. */
    int top() {
        //        int size = q.size();
//        for (int i = 0; i < size - 1; i ++) {
        for (int i = 0; i < q.size() - 1; i ++) {
            int front = q.front();
            q.pop();
            q.push(front);
        }
        int back = q.front();
        q.pop();
        q.push(back);
        return back;
    }

    /** Returns whether the stack is empty. */
    bool empty() {
        return q.empty();
    }
};


int main() {
    //Your MyStack object will be instantiated and called as such:
  MyStack* obj = new MyStack();
  obj->push(1);
  obj->push(2);
  obj->push(3);
  obj->push(4);
  int param_2 = obj->pop();
  int param_3 = obj->top();
  bool param_4 = obj->empty();
  printf("%d, %d, %d", param_2, param_3, param_4);
}
