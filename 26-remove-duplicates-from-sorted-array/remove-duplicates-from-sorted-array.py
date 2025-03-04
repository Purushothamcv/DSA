class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        k=1
        count=0
        for i in range(1,n):
            if nums[i-1]!=nums[i]:
                nums[k]=nums[i]
                k+=1
        return k



        