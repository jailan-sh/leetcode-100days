class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        if not operations:
            return 0
        stack = []
        operators = ('D', '+', 'C')
        for item in operations:
            if item not in operators:
                stack.append(int(item))
            else:
                if stack:
                    if item == 'C':
                        stack.pop()
                    elif item == 'D':
                        stack.append((2 * stack[-1]))
                    else:
                        if len(stack)== 1:
                            continue
                        else:
                            stack.append(stack[-1] + stack[-2])
        result = sum(stack)
        return result
