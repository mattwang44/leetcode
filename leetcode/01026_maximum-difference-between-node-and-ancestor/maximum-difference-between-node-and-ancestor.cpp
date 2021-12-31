/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxAncestorDiff(TreeNode* root) {
        return helper(root, root->val, root->val);
    }
    int helper(TreeNode* node, int _min, int _max) {
        if (node == NULL) {
            return _max - _min;
        }
        _max = max(node->val, _max);
        _min = min(node->val, _min);
        int l_diff = helper(node->left, _min, _max);
        int r_diff = helper(node->right, _min, _max);
        return max(l_diff, r_diff);
    }
};
