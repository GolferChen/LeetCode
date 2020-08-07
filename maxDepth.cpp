
//
// Created by Golfer on 2020/8/7.
//

#include <cstdio>
#include <clocale>
#include<algorithm>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
      int val;
     TreeNode *left;
     TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };

// Down-Top
//class Solution {
//public:
//    int maxDepth(TreeNode* root) {
//        if (! root)
//            return 0;
//        int left_max_depth = maxDepth(root->left);
//        int right_max_depth = maxDepth(root->right);
////        return max(left_max_depth, right_max_depth) + 1;
//        return (left_max_depth > right_max_depth) ? left_max_depth + 1 : right_max_depth + 1;
//    }
//};

// Top-Down
class Solution {
public:
    int max_depth = 0;
    int maxDepth(TreeNode* root) {
        get_max(root, max_depth + 1);
        return max_depth;
    }
    void get_max(TreeNode* cur, int depth) {
        if (! cur)
            return;
        if (! cur->left && ! cur->right) {
            max_depth = max(max_depth, depth);
        }
        get_max(cur->left, depth + 1);
        get_max(cur->right, depth + 1);
    }
};