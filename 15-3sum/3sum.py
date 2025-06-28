class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets=[]
        nums.sort()
        for i,value in enumerate(nums):
            if i>0 and (value==nums[i-1]):
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                current_sum=value+nums[left]+nums[right]
                if current_sum<0:
                    left+=1
                elif current_sum>0:
                    right-=1
                else:
                    triplets.append([value,nums[left],nums[right]])
                    left+=1
               
                    while (left<right) and nums[left]==nums[left-1]:
                        left+=1
                    while (left<right) and nums[right]==nums[right-1]:
                        right-=1
        return triplets
                

        