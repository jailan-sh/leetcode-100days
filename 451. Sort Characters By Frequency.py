class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequent = {}
        order = []
        for char in s:
            frequent[char] = frequent.get(char, 0) + 1
        char_sort = sorted(frequent, key=lambda x: frequent[x], reverse=True)
        for char in char_sort:
            char_f = char * frequent[char]
            order.append(char_f)
        return ''.join(order)
