class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        n = len(arr2)
        count = 0
        for num in arr1:
            h = n -1
            l = 0
            while l <= h:
                mid = (l + h) // 2
                if abs(num - arr2[mid]) <= d:
                    break
                elif num > arr2[mid]:
                    l = mid + 1
                else:
                    h = mid - 1
            else:
                count += 1
        return count
