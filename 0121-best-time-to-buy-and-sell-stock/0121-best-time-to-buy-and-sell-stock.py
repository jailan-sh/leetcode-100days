class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minmum = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            minmum = min(minmum, prices[i])
            profit = max(profit, (prices[i] - minmum))
        return profit