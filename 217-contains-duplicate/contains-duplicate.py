class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a={}
        for i in range(len(nums)):
            if nums[i] in a:
                return True 
            a[nums[i]]=i
        return False