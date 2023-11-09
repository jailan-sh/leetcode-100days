class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = collections.Counter(nums)
        unique = set(nums)
        for i in unique:
            if dic[i] > (len(nums)/2):
                return i

        