class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        f = 0
        b = len(height) - 1
        max_area = 0
        while f < b:
            area = min(height[f], height[b]) * (b - f)
            max_area = max(max_area, area)
            if height[f] < height[b]:
                f += 1
            else:
                b -= 1
        return (max_area)

