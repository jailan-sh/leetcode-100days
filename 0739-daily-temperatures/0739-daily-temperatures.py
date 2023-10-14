class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        answer = [0] * len(temperatures)
        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][1]:
                i_result = stack.pop()[0]
                answer[i_result] = index - i_result
            stack.append((index,value))
        return answer

