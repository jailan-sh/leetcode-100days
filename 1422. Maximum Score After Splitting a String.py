class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        zero_count = 0
        max_count = 0
        remain = s.count('1')
        for i in s[:-1]:
            if i == '0':
                zero_count += 1
            else:
                remain -= 1
            res = remain + zero_count
            max_count = max(max_count, res)
        return max_count
