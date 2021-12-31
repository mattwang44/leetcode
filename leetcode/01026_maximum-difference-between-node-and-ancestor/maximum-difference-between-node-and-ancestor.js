/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxAncestorDiff = function(root) {
    return helper(root, root.val, root.val);
};

var helper = function(node, _min, _max) {
    if (node === null) {
        return _max - _min;
    };
    _min = Math.min(node.val, _min);
    _max = Math.max(node.val, _max);
    const l_diff = helper(node.left, _min, _max);
    const r_diff = helper(node.right, _min, _max);
    return Math.max(l_diff, r_diff);
};