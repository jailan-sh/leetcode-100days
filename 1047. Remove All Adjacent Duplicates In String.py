class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)  
