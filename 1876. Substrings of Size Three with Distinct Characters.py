class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            if (len(s) - i) >= 3:
                sub = s[i:i+3]
                if len(sub) == len(set(sub)):
                    count += 1
        return count
