class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 1
        while x < n:
            x = (x << 1) | 1  # Shift left and set all lower bits
        return x
        