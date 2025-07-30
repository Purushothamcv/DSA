class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        max_prod = nums[0]
        curr_max, curr_min = nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                curr_max, curr_min = curr_min, curr_max
            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)
            max_prod = max(max_prod, curr_max)

        return max_prod

        # second method
        # n=len(nums)
        # maxx=float('-inf')
        # if len(nums)==1:
        #     return nums[0]
        # for i in range(n):
        #     mul=1
        #     for j in range(i,n):
        #         mul*=nums[j]
        #         maxx=max(mul,maxx)
        # return maxx
        # a=[]
        # def mul(a,b):
        #     c=a*b
        #     return c
        # for i in range(n):
        #     for j in range(i,n):
        #         a.append(nums[i:j+1])
        # mull=1
        # for i in a:
        #     for j in i:
        #         mull*=nums[j]
        # return mull



                

        