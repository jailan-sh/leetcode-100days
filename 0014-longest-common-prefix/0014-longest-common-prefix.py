class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        start = strs[0]
        for i in range(len(start)):
            char = start[i]
            for string in strs:
                if string[i] != char:
                    return start[:i]
                    break

        return start

