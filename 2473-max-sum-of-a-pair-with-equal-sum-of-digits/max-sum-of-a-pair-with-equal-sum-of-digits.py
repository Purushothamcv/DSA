class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -1  # Default value if no valid pairs exist
        digit_sum_map = {}  # Dictionary to store max numbers for each digit sum

        def digit_sum(n):
            """ Function to calculate sum of digits of a number """
            return sum(int(digit) for digit in str(n))

        for num in nums:
            s = digit_sum(num)  # Get sum of digits
            if s in digit_sum_map:
                max_sum = max(max_sum, num + digit_sum_map[s])  # Update max sum
                digit_sum_map[s] = max(digit_sum_map[s], num)  # Store max value for this sum
            else:
                digit_sum_map[s] = num  # Store first occurrence

        return max_sum
