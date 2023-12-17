class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num == 1:
            return True
        elif num < 0:
            return False
        l, r = 0, num
        while l <= r:
            mid = (l + r) // 2
            squ = mid * mid
            if num == squ:
                return True
            elif squ < num:
                l = mid + 1
            else:
                r = mid - 1
        return False
