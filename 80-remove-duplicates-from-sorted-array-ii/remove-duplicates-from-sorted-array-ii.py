class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        i=0
        count=1
        for j in range(1,len(nums)):
            if nums[j]==nums[j-1]:
                count+=1
            else:
                count=1
            if count<=2:
                i+=1
                nums[i]=nums[j]
                
        return i+1

        