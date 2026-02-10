class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxx = 0
        
        for i in range(n):
            evenset = set()
            oddset = set()
            
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    evenset.add(nums[j])
                else:
                    oddset.add(nums[j])
                
                if len(evenset) == len(oddset):
                    maxx = max(maxx, j - i + 1)
        
        return maxx
