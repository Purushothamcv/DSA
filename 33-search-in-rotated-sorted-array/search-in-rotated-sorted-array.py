class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # start=0
        # n=len(nums)
        # end=n-1

        # while start<=end:
        #     mid=(start+end)//2
        #     if nums[mid]==target:
        #         return mid
        #     if nums[start]<=nums[mid]:
        #         if nums[mid]>target>=nums[start]:
        #             end=mid-1
        #         else:
        #             start=mid+1
        #     else:
        #         if nums[mid]<target<=nums[end]:
        #             start=mid+1
        #         else:
        #             end=mid-1
                
        # return -1
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1