class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dic = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if words[i] in dic.values():
                    return False
                dic[pattern[i]] = words[i]
            else:
                if dic[pattern[i]] != words[i]:
                    return False
        return True