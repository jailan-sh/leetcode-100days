# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        left_side = self.invertTree(root.left)
        right_side= self.invertTree(root.right)

        root.left, root.right = (right_side, left_side)
        return root
        