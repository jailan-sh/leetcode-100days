class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        charmape = {}
        for char in magazine:
            charmape[char] = charmape.get(char, 0) + 1
        for char in ransomNote:
            if char in charmape and charmape[char] > 0:
                charmape[char] -= 1
            else:
                return False
        return True
