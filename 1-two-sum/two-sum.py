class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None:
            return -1
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                x=nums[j]
                # if nums[i-1]+nums[i]==target:
                #     return [i-1,i]
                if nums[i]+x==target:
                    return [i,j]
        


        return -1
        