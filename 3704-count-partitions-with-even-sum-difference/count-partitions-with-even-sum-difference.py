class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        left=0
        right=0
        count=0
        for i in range(n-1):
            left+=nums[i]
            right=sum(nums)-left
            if (left-right) % 2==0:
                count+=1
        return count


        

        