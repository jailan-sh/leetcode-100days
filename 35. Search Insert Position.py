class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        if target < nums[l]:
            return 0
        elif nums[r] < target:
            return r + 1
        else: 
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid -1
                else:
                    l = mid + 1
            return l
