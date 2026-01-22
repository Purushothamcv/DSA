class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minn=float('inf')
        max_profit=0
        for p in range(1,len(prices)):
            if prices[p]>prices[p-1]:
                max_profit+=prices[p]-prices[p-1]
        return max_profit