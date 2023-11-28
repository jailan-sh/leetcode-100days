class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [set("qwertyuiop"),
               set("asdfghjkl"),
               set("zxcvbnm")]
        result = []
        for word in words:
            new = word.lower()
            if any(set(new) <= row for row in rows):
                result.append(word)
        return result
