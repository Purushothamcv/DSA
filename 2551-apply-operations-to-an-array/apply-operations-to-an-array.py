class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        a = []
        b = []
        c = []
        i=0
        while i<n-1:
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
                a.append(nums[i])
                a.append(nums[i + 1])
                i+=2
            else:
                a.append(nums[i])
                i+=1
        if i==n-1:
            a.append(nums[i])
        for num in a:
            if num!=0:
                b.append(num)
            else:
                c.append(num)
        return b+c  