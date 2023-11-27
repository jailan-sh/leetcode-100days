class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []
        num_dic = {}
        for item in nums1:
            num_dic[item] = num_dic.get(item, 0) + 1
        for num in nums2:
            if num in num_dic and num_dic[num] > 0:
                intersection.append(num)
                num_dic[num] -= 1
        return intersection
