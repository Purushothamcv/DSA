class Solution:
    def findSmallestInteger(self, nums, value):
        # Step 1: Build remainder frequency dictionary
        freq = {}
        for num in nums:
            remainder = num % value
            # handle negative numbers correctly
            remainder = (remainder + value) % value
            freq[remainder] = freq.get(remainder, 0) + 1
        
        # Step 2: Find MEX
        mex = 0
        while True:
            remainder = mex % value
            if remainder in freq and freq[remainder] > 0:
                freq[remainder] -= 1
                mex += 1
            else:
                return mex
