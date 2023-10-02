class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        f = 0
        r = len(numbers) - 1
        while 1:
            if numbers[f] + numbers[r] > target:
                r -= 1
            elif numbers[f] + numbers[r] < target:
                f += 1
            else:
                return sorted([f +1, r+1])
        