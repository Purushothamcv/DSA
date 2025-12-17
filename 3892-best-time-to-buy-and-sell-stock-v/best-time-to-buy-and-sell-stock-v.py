class Solution:
    def maximumProfit(self, prices, k):
        n = len(prices)
        INF = float('-inf')

        # dp[t][state]
        # state 0: idle
        # state 1: holding long (bought)
        # state 2: holding short (sold)
        dp = [[INF] * 3 for _ in range(k + 1)]
        dp[0][0] = 0  # start idle with 0 profit

        for price in prices:
            new_dp = [row[:] for row in dp]

            for t in range(k + 1):
                # From idle → buy (start normal transaction)
                new_dp[t][1] = max(new_dp[t][1], dp[t][0] - price)

                # From idle → sell (start short transaction)
                new_dp[t][2] = max(new_dp[t][2], dp[t][0] + price)

                if t < k:
                    # From long → sell (finish normal transaction)
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][1] + price)

                    # From short → buy back (finish short transaction)
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][2] - price)

            dp = new_dp

        # Best profit with at most k completed transactions, idle state
        return max(dp[t][0] for t in range(k + 1))
