class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<nums[right]:
                right=mid
            else:
                left=mid+1
        return nums[right]      
            # if nums[left] == nums[mid] == nums[right]:
            #     left += 1
            #     right -= 1
            # elif nums[left]<=nums[mid]:
            #     if nums[left]<=target<nums[mid]:
            #         right=mid-1
            #     else:
            #         left=mid+1
            # else:
            #     if nums[mid]<target<=nums[right]:
            #         left=mid+1
            #     else:
            #         right=mid-1
        # return False


        