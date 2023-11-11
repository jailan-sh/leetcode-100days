class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if not word1:
            return word2
        elif not word2:
            return word1
        result = ""
        i = 0
        while i < min(len(word1), len(word2)):
            p1 = word1[i]
            p2 = word2[i]
            result += p1 + p2
            i += 1
        remain = word1[i:] if len(word1) > len(word2) else word2[i:]
        result += remain
        return result
