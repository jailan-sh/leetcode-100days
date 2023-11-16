class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapy = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in mapy:
                if t[i] not in mapy.values():
                    mapy[s[i]] = t[i]
                else:
                    return False
            elif mapy[s[i]] != t[i]:
                    return False
        return True
