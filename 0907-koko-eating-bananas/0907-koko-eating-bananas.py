class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            time = sum((pile-1) // mid + 1 for pile in piles)
            if time > h:
                left = mid + 1
            else:
                right = mid
        return left


        
        