class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        x={}
        # for i in range(n):
        #     if nums[i] in x:
        #         x[nums[i]]=1
        #     else:
        #         x[nums[i]]+=1
        # for i,value in enumerate(x.items()):
        #     if value>1:
        #         return i
        for key in nums:
            x[key]=x.get(key,0)+1
        for key,value in x.items():
            if value>1:
                return key
