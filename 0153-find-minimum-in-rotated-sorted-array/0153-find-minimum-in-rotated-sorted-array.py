class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) -1
        if len(nums) == 1:
            return nums[0]
        if nums[lo] < nums[hi]:
            return nums[lo]
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid+1] and nums[mid] < nums[mid -1]:
                return nums[mid]
            elif nums[mid] > nums[mid + 1]:
                return nums[mid+1]
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1