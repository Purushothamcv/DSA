class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        l=0
        total=0
        min_l=float('inf')
        for i in range(n):
            total+=nums[i]
            while total>=target:
                min_l=min(min_l,i-l+1)
                total-=nums[l]
                l+=1
        if min_l==float('inf'):
            return 0
        return min_l

                

