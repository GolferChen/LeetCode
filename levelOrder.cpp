//
// Created by Golfer on 2020/8/7.
//


#include <clocale>
#include <vector>
#include <queue>
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<pair<int, TreeNode*>> q;
        vector<vector<int>> output;
        q.push(make_pair(0, root));
        while (! q.empty()) {
            pair<int, TreeNode*> cur = q.front();
            q.pop();
            int cur_level = cur.first;
            TreeNode* cur_node = cur.second;
            if (! cur_node)
                continue;
            if (output.size() == cur_level)
                output.push_back(vector<int>{cur_node->val});
            else
                output[cur_level].push_back(cur_node->val);
            if (cur_node->left)
                q.push(make_pair(cur_level+1, cur_node->left));
            if (cur_node->right)
                q.push(make_pair(cur_level+1, cur_node->right));
        }
        return output;
    }
};

