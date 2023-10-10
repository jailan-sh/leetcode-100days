class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closeToOpen = {")": "(", "}": "{", "]": "["}
        stack = []
        if len(s) % 2 != 0:
            return False
        for c in s:
            if c in ('[', '(', '{'):
                stack.append(c)
            else:
                if c in closeToOpen:
                    if stack and stack[-1] == closeToOpen[c]:
                        stack.pop()
                    else:
                        return False
        return not stack 
        