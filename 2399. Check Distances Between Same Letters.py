class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        checker = {}
        for i in range(len(s)):
            if s[i] not in checker:
                checker[s[i]] = i
            else:
                if (i - checker[s[i]] - 1) == distance[ord(s[i]) - ord('a')]:
                    checker[s[i]] = i
                else:
                    return False
        return True
