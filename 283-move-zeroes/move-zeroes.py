class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n=len(nums)
    
        # left=0
        # right=0
        # for right in range(n):
        #     if nums[right]!=0:
        #         nums[right],nums[left]=nums[left],nums[right]
        #         right+=1
        #         left+=1
        #     right+=1
        # return nums
        a=[]
        left=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[left],nums[i]=nums[i],nums[left]
                left+=1
        return nums
        