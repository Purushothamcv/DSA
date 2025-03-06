class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        size = n * n
        freq = [0] * (size + 1)
        
        for row in grid:
            for num in row:
                freq[num] += 1
        
        a, b = -1, -1
        for num in range(1, size + 1):
            if freq[num] == 2:
                a = num
            elif freq[num] == 0:
                b = num
        
        return [a, b]