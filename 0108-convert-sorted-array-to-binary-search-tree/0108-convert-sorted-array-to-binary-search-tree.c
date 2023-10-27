/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* add(int* nums, int start, int end) {
    if (start > end) {
        return NULL;
    }

    int mid = start + (end - start) / 2;

    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = nums[mid];
    root->left = add(nums, start, mid - 1);
    root->right = add(nums, mid + 1, end);

    return root;
}

struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    return add(nums, 0, numsSize - 1);
}