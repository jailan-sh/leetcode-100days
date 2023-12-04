class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -1 * nums[index]
            else:
                result.append(abs(num))
        return result

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicate = {}
        result = []
        for num in nums:
            duplicate[num] = duplicate.get(num, 0) + 1
        for k , v in duplicate.items():
            if v == 2:
                result.append(k)
        return result
