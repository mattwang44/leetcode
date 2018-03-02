// 1st try: Jan. 26, 2018
// https://leetcode.com/problems/invert-binary-tree/description/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root || (!root->left && !root->right)) return root;
        swap(root->left, root->right);
        invertTree(root->right);
        invertTree(root->left);       
        return root;
    }
};