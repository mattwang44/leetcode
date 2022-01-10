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
    int sumRootToLeaf(TreeNode* root) {
        return helper(root, 0);
    }

private:
    int helper(TreeNode* node, int accumulate) {
        if (node == NULL) {
            return 0;
        }

        accumulate = accumulate * 2 + node->val;
        if (!node->left && !node->right) {
            return accumulate;
        }

        return helper(node->left, accumulate) + helper(node->right, accumulate);
    }
};
