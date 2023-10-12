class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ("+", "-", "/", "*")
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num1 = stack.pop(-2)
                num2 = stack.pop()
                if token == "+":
                    result = num1 + num2
                elif token == "-":
                    result = num1 - num2
                elif token == "*":
                    result = num1 * num2
                else:
                    result = int(float(num1)/num2)
                stack.append(result)
        return stack[0]
