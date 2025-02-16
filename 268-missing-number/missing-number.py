class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        y=n
        x=int(y*(y+1)//2)
        return x-sum(nums)
        