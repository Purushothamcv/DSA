class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        # nums1=sorted(nums)
        for i in nums:
            a.append(i*i)
        a1=sorted(a)
        return a1
        