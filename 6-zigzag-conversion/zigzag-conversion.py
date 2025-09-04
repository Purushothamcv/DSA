class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge case: if only one row or fewer rows than string length
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur_row, step = 0, -1

        for char in s:
            rows[cur_row] += char
            # Change direction at top or bottom
            if cur_row == 0 or cur_row == numRows - 1:
                step *= -1
            cur_row += step

        return "".join(rows)
