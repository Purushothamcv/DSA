class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=float('inf')
        max_profit=0
        n=len(prices)
        for p in prices:
            if p<min_price:
                min_price=p
            profit=p-min_price
            max_profit=max(max_profit,profit)
            if max_profit<0:
                return 0
        return max_profit
        