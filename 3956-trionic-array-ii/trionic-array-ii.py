class Solution:
    def maxSumTrionic(self, nums):
        n = len(nums)
        INF = float('-inf')

        dp0 = nums[0]          # start state
        dp1 = INF              # first increasing
        dp2 = INF              # decreasing
        dp3 = INF              # second increasing (valid)

        ans = INF

        for i in range(1, n):

            new_dp0 = nums[i]
            new_dp1 = INF
            new_dp2 = INF
            new_dp3 = INF

            if nums[i] > nums[i - 1]:
                # First increasing
                new_dp1 = max(
                    dp1 + nums[i] if dp1 != INF else INF,
                    dp0 + nums[i]
                )

                # Second increasing
                if dp3 != INF:
                    new_dp3 = dp3 + nums[i]
                if dp2 != INF:
                    new_dp3 = max(new_dp3, dp2 + nums[i])

            if nums[i] < nums[i - 1]:
                # Decreasing
                if dp2 != INF:
                    new_dp2 = dp2 + nums[i]
                if dp1 != INF:
                    new_dp2 = max(new_dp2, dp1 + nums[i])

            dp0, dp1, dp2, dp3 = new_dp0, new_dp1, new_dp2, new_dp3

            ans = max(ans, dp3)

        return ans
