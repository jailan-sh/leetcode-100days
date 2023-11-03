# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        h_r = self.diameterOfBinaryTree(root.right)
        h_l = self.diameterOfBinaryTree(root.left)

        lside = self.depth(root.left)
        rside = self.depth(root.right)
        return max(max(h_r, h_l), lside + rside)

    def depth(self, root):
        if not root:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        return max(left_depth, right_depth) + 1