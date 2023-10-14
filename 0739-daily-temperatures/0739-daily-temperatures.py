class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures [i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                days = i - prev_index
                answer[prev_index] = days
            stack.append(i)
        return answer

