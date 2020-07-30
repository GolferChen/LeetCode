//
// Created by Golfer on 2020/7/26.
//


#include <clocale>
#include <vector>
#include <stack>
#include <set>

using namespace std;

// Definition for a binary tree node.
 struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> orders;
        if (root == NULL) {
            return orders;
        }
        if (root->left == NULL && root->right ==NULL) {
            orders.push_back(root->val);
            return orders;
        }
        stack<TreeNode*> s;
        s.push(root);
        TreeNode* cur = root;
        set<TreeNode*> visited;
//        vector<int> orders;
        while (s.size() > 0) {
            while (cur->left && visited.find(cur->left) == visited.end()) {
                cur = cur->left;
                s.push(cur);
            }
            TreeNode* v = s.top();
            s.pop();
            orders.push_back(v->val);
            visited.insert(v);
            if (v->right) {
                cur = v->right;
                s.push(cur);
            }
            else {
                if (s.size() > 0) {
                    cur = s.top();
                }
            }
        }
        return orders;
    }
};

