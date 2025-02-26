class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=current_max=min_sum=current_min=0
        for num in nums:
            current_max=max(current_max+num,num)
            max_sum=max(current_max,max_sum)
            current_min=min(current_min+num,num)
            min_sum=min(current_min,min_sum)
        return max(max_sum,abs(min_sum))

        
        