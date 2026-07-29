class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # l=0
        # r=len(nums)-1
        # a=[]
        # nums.sort()
        # while l<r:
        #     for i in range(l+1,r):
        #         summ=nums[l]+nums[i]+nums[r]
        #         if summ==0:
        #             a.append([nums[l],nums[i],nums[r]])
        #     if summ>0:
        #         r-=1
        #     else:
        #         l+=1
        #     # r-=1
        #     # l+=1
        # return a
        # n=len(nums)
        # a=[]
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 a.append([nums[i],nums[j],nums[k]])
        # return a
        n=len(nums)
        nums.sort()
        a=[]
        for i in range(len(nums)-2):
            l=i+1
            r=n-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l<r:
                summ=nums[i]+nums[l]+nums[r]
                if summ==0:
                    a.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==[nums[l-1]]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif summ<0:
                    l+=1
                else:
                    r-=1
        return a
                
                

        