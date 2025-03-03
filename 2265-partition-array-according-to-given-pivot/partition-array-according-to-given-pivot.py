class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        n=len(nums)
        a=[]
        b=[]
        c=[]
        for i in range(n):
            if nums[i]<pivot:
                b.append(nums[i])
            elif nums[i]==pivot:
                a.append(nums[i])
            else:
                c.append(nums[i])
        return b+a+c


        