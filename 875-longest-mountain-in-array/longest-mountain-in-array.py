class Solution(object):
    def longestMountain(self, nums):
        """
        :type arr: List[int]
        :rtype: int
        """
        res=0
        n=len(nums)
        for i in range(1,n-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                l=r=i
                while l>0 and nums[l]>nums[l-1]:
                    l-=1
                while r<n-1 and nums[r]>nums[r+1]:
                    r+=1
                res=max(res,r-l+1)
        return res
