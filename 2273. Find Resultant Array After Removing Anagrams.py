class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        collect = {}
        result = []
        for i in range(len(words)):
            new = ''.join(sorted(words[i]))
            if new not in collect:
                collect[new] = words[i]
                result.append(words[i])
            else:
                pre = ''.join(sorted(words[i-1]))
                if new in collect and new != pre:
                    result.append(words[i])
        return result
