class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        left = 0
        count = 0
        prefix_sum = {0: 1}  # To handle cases where summ == goal
        summ = 0

        for right in range(len(nums)):
            summ += nums[right]
            
            # Check if (summ - goal) exists in prefix_sum
            if (summ - goal) in prefix_sum:
                count += prefix_sum[summ - goal]
            
            # Add/update prefix_sum dictionary
            prefix_sum[summ] = prefix_sum.get(summ, 0) + 1

        return count
