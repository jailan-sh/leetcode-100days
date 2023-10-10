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
        for c in range(len(s)):
            if s[c] in ('[', '(', '{'):
                stack.append(s[c])
            else:
                if s[c] in closeToOpen:
                    if stack and stack[-1] == closeToOpen[s[c]]:
                        stack.pop()
                    else:
                        return False
        return not stack 
        