class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atMostK(nums, k):
            count = {}
            left = 0
            res = 0
            for right in range(len(nums)):
                if nums[right] not in count or count[nums[right]] == 0:
                    k -= 1
                count[nums[right]] = count.get(nums[right], 0) + 1

                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1
                res += right - left + 1
            return res
        
        return atMostK(nums, k) - atMostK(nums, k - 1)
