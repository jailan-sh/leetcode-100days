class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mape = {"I": 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M':1000}
        num = 0
        for i in range(len(s) - 1):
            if mape[s[i]] < mape[s[i + 1]]:
                num -= mape[s[i]]
            else:
                num += mape[s[i]]
        num += mape[s[-1]] 
        return num
    