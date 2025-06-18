class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum=nums[0]
        max_sum=nums[0]
        for i in nums[1:len(nums)]:
            current_sum=max(i,current_sum+i)
            max_sum=max(current_sum,max_sum)
        return max_sum