class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        current = 0  # streak of consecutive zeros
        
        for num in nums:
            if num == 0:
                current += 1      # extend zero streak
                count += current  # add subarrays ending here
            else:
                current = 0       # reset if non-zero
                
        return count
