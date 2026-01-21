class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for x in nums:
            # If x is even (only possible prime is 2), no solution
            if x % 2 == 0:
                ans.append(-1)
                continue

            # Count trailing 1s in binary representation of x
            t = 0
            temp = x
            while temp & 1:
                t += 1
                temp >>= 1

            # Minimum possible value
            ans.append(x - (1 << (t - 1)))

        return ans
