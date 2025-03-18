class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        count=0
        x=0
        n=len(nums)
        maxcount=0
        for right in range(n):
            if nums[right]==0:
                x+=1
            while x>k:
                if nums[left]==0:
                    x-=1
                left+=1
            maxcount=max(maxcount,right-left+1)
        return maxcount
        


        