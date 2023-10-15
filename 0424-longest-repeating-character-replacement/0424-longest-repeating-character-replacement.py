class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_count = [0] * 26
        longest = 0
        l = 0
        max_count = 0
        for r in range(len(s)):
            char_count[ord(s[r]) - ord('A')] += 1
            if (r - l + 1) - max(char_count) > k:
                char_count[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, r - l +1)
        return longest