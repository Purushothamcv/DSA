class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        x={}
        for i,val in enumerate(nums):
            if val in x and i-x[val]<=k:
                return True
            x[val]=i
        return False

        