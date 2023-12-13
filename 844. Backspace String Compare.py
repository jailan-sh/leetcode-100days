class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def compare(lis, st):
            for i in range(len(st)):
                if st[i] == '#':
                    if lis:
                        lis.pop()
                    else:
                        continue
                else:
                    lis.append(st[i])
            return lis
        
        stack1 =[]
        stack2 = []
        return compare(stack1, s) == compare(stack2, t)

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def compare(st):
            stack = []
            for i in range(len(st)):
                if st[i] == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(st[i])
            return ''.join(stack)
        return compare(s) == compare(t)
