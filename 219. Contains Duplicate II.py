class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        unique = set(nums)    
        if len(unique) == len(nums):
            return False
        else:
            duplicate = {}
            for i in range(len(nums)):
                if nums[i] in duplicate and abs(i -duplicate[nums[i]]) <= k:
                   return True
                duplicate[nums[i]] = i
        return False
