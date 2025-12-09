class Solution(object):
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        
        # Count frequency of all numbers on the right initially
        right = {}
        for x in nums:
            right[x] = right.get(x, 0) + 1
        
        left = {}
        ans = 0
        
        for j in range(n):
            val = nums[j]

            # j is the middle element, so remove it from right
            right[val] -= 1
            if right[val] == 0:
                del right[val]
            
            # We want i < j such that nums[i] = 2 * nums[j]
            # and k > j such that nums[k] = 2 * nums[j]
            target = val * 2
            
            left_count = left.get(target, 0)
            right_count = right.get(target, 0)
            
            ans = (ans + left_count * right_count) % MOD
            
            # Move nums[j] into left map
            left[val] = left.get(val, 0) + 1
        
        return ans
