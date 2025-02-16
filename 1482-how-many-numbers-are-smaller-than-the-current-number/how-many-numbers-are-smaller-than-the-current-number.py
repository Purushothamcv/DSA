class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        y=sorted(nums)
        # return nums
        a={}
        x=[]
        for i,value in enumerate(y):
            if value not in a:
                a[value]=i
        for num in nums:
            x.append(a[num])
        return x
        # return a
        