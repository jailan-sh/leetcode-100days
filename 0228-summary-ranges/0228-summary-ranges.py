class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        ranges = []
        start = end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                ranges.append(self.formatRange(start, end))
                start = end = nums[i]

        ranges.append(self.formatRange(start, end))
        return ranges

    def formatRange(self, start, end):
        if start == end:
            return str(start)
        else:
            return str(start) + "->" + str(end)
            