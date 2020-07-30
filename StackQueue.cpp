//
// Created by Golfer on 2020/7/26.
//

#include <stack>
#include <cstdio>
using namespace std;

//class MyQueue {
//public:
//    stack<int> s;
//    stack<int> s_help;
//    /** Initialize your data structure here. */
//    MyQueue() {
//
//    }
//
//    /** Push element x to the back of queue. */
//    void push(int x) {
//        s.push(x);
//    }
//
//    /** Removes the element from in front of queue and returns that element. */
//    int pop() {
////        if (s.empty()) { // not considering
////        }
////        for (int i = 0; i < s.size() - 1; i++) { // wrong since s.size() will change after pop() operation
////            int top = s.top();
////            s.pop();
////            s_help.push(top);
////        }
//
//
////        int top;
////        while (! s.empty()) {
////            top = s.top();
////            s.pop();
////            s_help.push(top);
////        }
////        int front = top;
////        s_help.pop(); // exclude the front
//
//          // optimization
//          int s_size = s.size();
//          for (int i = 0; i < s_size - 1; i++) { // we only need to push s.size() - 1 elements to s_help
//              int top = s.top();
//              s.pop();
//              s_help.push(top);
//          }
//          int front = s.top();
//          s.pop();
//
////        s.pop();
////        for (int i = 0; i < s_help.size(); i++) {
////            int top = s_help.top();
////            s_help.pop();
////            s.push(top);
////        }
//        while (! s_help.empty()) {
//            int top = s_help.top();
//            s_help.pop();
//            s.push(top);
//        }
//        return front;
//    }
//
//    /** Get the front element. */
//    int peek() {
////        if (s.empty()) { // not considering
////        }
//        int top;
////        for (int i = 0; i < s.size(); i++) {
////            top = s.top();
////            s.pop();
////            s_help.push(top);
////        }
//        while (! s.empty()) {
//            top = s.top();
//            s.pop();
//            s_help.push(top);
//        }
//        int front = top;
////        for (int i = 0; i < s_help.size(); i++) {
////            int top = s_help.top();
////            s_help.pop();
////            s.push(top);
////        }
//        while (! s_help.empty()) {
//            int top = s_help.top();
//            s_help.pop();
//            s.push(top);
//        }
//        return front;
//    }
//
//    /** Returns whether the queue is empty. */
//    bool empty() {
//        return s.empty();
//    }
//};

// Version Two
class MyQueue {
public:
    stack<int> s;
    stack<int> s_help;
    /** Initialize your data structure here. */
    MyQueue() {

    }

    /** Push element x to the back of queue. */
    void push(int x) {
        s.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if (! s_help.empty()) {
            int front = s_help.top();
            s_help.pop();
            return front;
        }
//        if (s.empty()) { // both s_help and s are empty
//        }
        int s_size = s.size();
        for (int i = 0; i < s_size - 1; i++) {
            int top = s.top();
            s.pop();
            s_help.push(top);
        }
        int front = s.top();
        s.pop();
        return front;
    }

    /** Get the front element. */
    int peek() {
        if (! s_help.empty()) {
            int front = s_help.top();
            return front;
        }
//        if (s.empty()) { // both s_help and s are empty
//        }
        int s_size = s.size();
        for (int i = 0; i < s_size; i++) {
            int top = s.top();
            s.pop();
            s_help.push(top);
        }
        int front = s_help.top();
        return front;
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return (s.empty() && s_help.empty());
    }
};

int main() {

// Your MyQueue object will be instantiated and called as such:
 MyQueue* obj = new MyQueue();
 obj->push(1);
 obj->push(2);
 int param_2 = obj->peek();
 int param_3 = obj->pop();
 bool param_4 = obj->empty();
 printf("%d, %d, %d", param_2, param_3, param_4);
 }
/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */