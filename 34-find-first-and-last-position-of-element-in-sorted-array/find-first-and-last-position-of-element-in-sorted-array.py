class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_first(nums, target):
            start, end = 0, len(nums) - 1
            first = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    first = mid  # Update first occurrence
                    end = mid - 1  # Keep searching on the left
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return first

        def find_last(nums, target):
            start, end = 0, len(nums) - 1
            last = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    last = mid  # Update last occurrence
                    start = mid + 1  # Keep searching on the right
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return last

        return [find_first(nums, target), find_last(nums, target)]
