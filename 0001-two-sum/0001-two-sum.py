class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydic = {}
        for index, item in enumerate(nums):
            res = target - item
            if res in mydic:
                return [mydic[res], index]
            mydic[item] = index
           
        
        