class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma=float('-inf')
        if len(nums)==1:
            return nums[0]
        summ=float('-inf')
        best=float('-inf')
        for i in range(len(nums)):
            summ=max(nums[i],nums[i]+summ)
            best=max(summ,best)
        return best
                



        
