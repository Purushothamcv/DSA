class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # def prod(a):            
        # a=[]
        # count=0
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i,n):
        #         a.append(nums[i:j+1])
        # prod=1
        # for i in a:
        #     prod=1
        #     for j in i:
        #         prod*=j
        #     if prod<k:
        #         count+=1
        # return count
        left=0
        count=0
        prod=1
        for right in range(len(nums)):
            prod*=nums[right]
            while prod>=k and left<=right:
                prod//=nums[left]
                left+=1
            count+=(right-left+1)
        return count





        