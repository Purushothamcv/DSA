class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Counter for elements not equal to val
    
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move valid element to the front
                k += 1  # Increment count of valid elements
        
        return k