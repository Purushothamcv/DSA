class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        
        count1=0
        count=0
        count2=0
        for right in range(len(nums)):
            if nums[right]%2!=0:
                count+=1
                count1=0
                while count==k:
                    if nums[left]%2!=0:
                        count-=1
                    left+=1
                    count1+=1
            count2+=count1
        return count2