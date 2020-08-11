//
// Created by Golfer on 2020/8/11.
//

#include <vector>
#include <cstdio>
#include <map>
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
    map<int, int> val_index_map;
    queue<int> preorder_q;
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for (int index = 0; index < inorder.size(); index++) {
            val_index_map.insert(make_pair(inorder[index], index));
        }
        for (int & x : preorder)
            preorder_q.push(x);
        return helper(0, inorder.size()-1);
    }
    TreeNode* helper(int left, int right) {
        if (left > right)
            return NULL;
        int root_val = preorder_q.front();
        preorder_q.pop();
        int root_index = val_index_map[root_val];
//        TreeNode root_node = TreeNode(root_val); // struct, not class !!
//        TreeNode root_node(root_val);
//        TreeNode* root = & root_node;
        TreeNode* root = new TreeNode(root_val);
        root->left = helper(left, root_index-1);
        root->right = helper(root_index+1, right);
        return root;
    }
};

