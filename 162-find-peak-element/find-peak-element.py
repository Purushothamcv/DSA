class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        n=len(nums)
        end=n-1
        while start<end:
            mid=(start+end)//2
        
            if  nums[mid] > nums[mid+1] :
                end=mid
            else:
                start=mid+1
        return start
            
        