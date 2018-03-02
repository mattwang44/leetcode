class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (!t1 && !t2){return NULL;}
        TreeNode *node = new TreeNode((t1?t1->val:0)+(t2?t2->val:0));
        node->left  = mergeTrees(t1?t1->left:nullptr , t2?t2->left:nullptr );
        node->right = mergeTrees(t1?t1->right:nullptr, t2?t2->right:nullptr);
        return node;
    }    
};