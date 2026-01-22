class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # cnt=0
        # def merge_sort(nums):
        #     if len(nums)<=1:
        #         return nums
        #     mid=len(nums)//2
        #     left=merge_sort(nums[:mid])
        #     right=merge_sort(nums[mid:])
        #     return merge(left,right)
        
        # def merge(left, right):
        #     i = j = 0
        #     res = []

        #     while i < len(left) and j < len(right):
        #         if left[i] <= right[j]:
        #             res.append(left[i])
        #             i += 1
        #         else:
        #             res.append(right[j])
        #             j += 1
        #     res.extend(left[i:])
        #     res.extend(right[j:])
        #     return res
        def issorted(nums):
            for i in range(1,len(nums)):
                if nums[i]<nums[i-1]:
                    return False
            return True
        cnt=0
        while not issorted(nums) and len(nums)>1:
            min_sum=float('inf')
            idx=0
            
            for i in range(len(nums)-1):
                s= nums[i]+nums[i+1]
                if s<min_sum:
                    min_sum=s
                    idx=i
                    
                    
            nums.pop(idx+1)
            nums.pop(idx)
            nums.insert(idx,min_sum)
            cnt+=1
        return cnt
        # return 0

        