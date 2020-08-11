//
// Created by Golfer on 2020/8/11.
//

//
// Created by Golfer on 2020/8/11.
//

#include <vector>
#include <cstdio>
#include <map>
#include <queue>
#include <stack>
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
    map<int, int> val_index_map;
    stack<int> preorder_s;
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        for (int index = 0; index < inorder.size(); index++) {
            val_index_map.insert(make_pair(inorder[index], index));
        }
        for (int & x : postorder)
            preorder_s.push(x);
        return helper(0, inorder.size()-1);
    }
    TreeNode* helper(int left, int right) {
        if (left > right)
            return NULL;
        int root_val = preorder_s.top();
        preorder_s.pop();
        int root_index = val_index_map[root_val];
//        TreeNode root_node = TreeNode(root_val); // struct, not class !!
//        TreeNode root_node(root_val);
//        TreeNode* root = & root_node;
        TreeNode* root = new TreeNode(root_val);
        root->right = helper(root_index+1, right);
        root->left = helper(left, root_index-1);
        return root;
    }
};


