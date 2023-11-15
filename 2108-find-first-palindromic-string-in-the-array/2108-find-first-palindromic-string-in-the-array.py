class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for item in words:
            if item == item[::-1]:
                return item
        return ""