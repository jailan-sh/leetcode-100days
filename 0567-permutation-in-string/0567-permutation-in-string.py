class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        c1 = collections.Counter(s1)
        c2 = collections.Counter(s2[:l1])
        for i in range(l2 - l1):
            if c1 == c2:
                return True
            else:
                char1, char2 = s2[i], s2[i+l1]
                c2[char1] -=1
                c2[char2] += 1
                if c2[char1] == 0:
                    del c2[char1]
        return c1 == c2