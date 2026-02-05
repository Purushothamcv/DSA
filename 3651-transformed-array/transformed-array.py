class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        # i=0
        for i in range(len(nums)):
            if nums[i]==0:
                a.append(0)
            else:
                index=(i+nums[i])%len(nums)
                a.append(nums[index])
        return a