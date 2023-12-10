class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                f = j + 1
                b = len(nums) - 1
                while f < b:
                    aim = nums[i] + nums[j] + nums[f] + nums[b]
                    if aim > target:
                        b -=1
                    elif aim < target:
                        f +=1
                    else:
                        result. append([nums[i], nums[j], nums[f],nums[b]])
                        while f < b and nums[f] == nums[f+1]:
                            f +=1
                        while f < b and nums[b] == nums[b - 1]:
                            b -= 1
                        f += 1
                        b -= 1
        return result 
