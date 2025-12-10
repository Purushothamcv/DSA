class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
# x=0
        x = []
        for i in range(n ):
            x.append(nums[(n - k + i) % n])
        for i in range(n):
            nums[i]=x[i]
        
        