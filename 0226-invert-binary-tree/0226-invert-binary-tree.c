/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* invertTree(struct TreeNode* root){

    if (root == NULL){
        return root;
    }
    struct TreeNode* left_side;
    struct TreeNode* right_side;

    left_side = invertTree(root->left);
    right_side = invertTree(root->right);

    root->left = right_side;
    root->right = left_side;

    return (root);
}