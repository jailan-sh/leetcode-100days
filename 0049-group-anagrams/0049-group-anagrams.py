class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for item in strs:
            if  ''.join(sorted(item)) not in anagrams:
                anagrams[''.join(sorted(item))] = [item]
            else:
                anagrams[''.join(sorted(item))].append(item)         
        return list(anagrams.values())
        