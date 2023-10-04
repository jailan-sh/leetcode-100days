class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            f = i + 1
            b = len(nums) - 1
            while f < b:
                if nums[i] + nums[f] + nums[b] > 0:
                    b -=1
                elif nums[i] + nums[f] + nums[b] < 0:
                    f +=1
                else:
                    result.append([nums[i], nums[f], nums[b]])
                    while f<b and nums[f] == nums[f+1]:
                        f +=1
                    while f<b and nums[b] == nums[b-1]:
                        b -=1 
                    f +=1
                    b -=1
        return result
                 