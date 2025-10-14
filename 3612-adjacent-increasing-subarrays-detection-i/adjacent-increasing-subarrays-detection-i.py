class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        def is_increasing(start):
            # Check if subarray nums[start : start + k] is strictly increasing
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True

        n = len(nums)

        # We need two adjacent increasing subarrays of length k
        # So we check subarrays starting at i and i + k
        for i in range(n - 2 * k + 1):
            if is_increasing(i) and is_increasing(i + k):
                return True

        return False
