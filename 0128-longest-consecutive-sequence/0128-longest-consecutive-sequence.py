class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_sequence = 0
        unique_nums = set(nums)
        for num in nums: 
            if num - 1 not in unique_nums:
                current_num = num
                count = 1
                while current_num + 1 in unique_nums:
                    current_num += 1
                    count += 1
                longest_sequence = max(longest_sequence, count)
        return longest_sequence