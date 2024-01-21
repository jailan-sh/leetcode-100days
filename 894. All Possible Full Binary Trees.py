# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        def backtrack(n):
            if n == 0:
                return []
            elif n == 1:
                return [TreeNode()]
            result = []
            for L in range(n):
                R = n-1-L
                left = backtrack(L)
                right = backtrack(R)
                for t1 in left:
                    for t2 in right:
                        result.append(TreeNode(0,t1,t2))
            return result
            
        return backtrack(n)
