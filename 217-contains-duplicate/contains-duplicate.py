class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=set()
        for i in range(len(nums)):
            if nums[i] in a:
                return True 
            a.add(nums[i])
        return False