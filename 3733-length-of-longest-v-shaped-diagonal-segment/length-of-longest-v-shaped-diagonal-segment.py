class Solution(object):
    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0

        # DP tables for straight segments starting with 1
        # s1: TL->BR, s2: TR->BL, s3: BL->TR, s4: BR->TL
        s1 = [[0] * m for _ in range(n)]
        s2 = [[0] * m for _ in range(n)]
        s3 = [[0] * m for _ in range(n)]
        s4 = [[0] * m for _ in range(n)]
        
        # DP tables for continuing segments
        # _co: continues odd-length seq, _ce: continues even-length seq
        s1_co, s1_ce = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]
        s2_co, s2_ce = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]
        s3_co, s3_ce = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]
        s4_co, s4_ce = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]
        
        max_len = 0

        def get_expected(length):
            # Sequence is 1, 2, 0, 2, 0, ...
            # For length > 1, it's 2 if length is even, 0 if length is odd.
            # (length - 1) is the 0-indexed position.
            # If (length - 1) is odd -> length is even -> expect 2
            # If (length - 1) is even -> length is odd -> expect 0
            if length <= 1: return -1 # Should not be called for length 1
            return 2 if (length - 1) % 2 != 0 else 0

        # Pass 1: Top-to-Bottom passes
        for r in range(n):
            # Forward C pass for s1 (TL->BR) and s4_cont (BR->TL)
            for c in range(m):
                if grid[r][c] == 1:
                    s1[r][c] = 1
                elif r > 0 and c > 0 and s1[r-1][c-1] > 0 and grid[r][c] == get_expected(s1[r-1][c-1] + 1):
                    s1[r][c] = s1[r-1][c-1] + 1
                if s1[r][c] > 0: max_len = max(max_len, s1[r][c])
                
                prev_co = s4_co[r-1][c-1] if r > 0 and c > 0 else 0
                prev_ce = s4_ce[r-1][c-1] if r > 0 and c > 0 else 0
                if grid[r][c] == 0: s4_ce[r][c] = 1 + prev_co
                if grid[r][c] == 2: s4_co[r][c] = 1 + prev_ce

            # Backward C pass for s2 (TR->BL) and s3_cont (BL->TR)
            for c in range(m - 1, -1, -1):
                if grid[r][c] == 1:
                    s2[r][c] = 1
                elif r > 0 and c < m - 1 and s2[r-1][c+1] > 0 and grid[r][c] == get_expected(s2[r-1][c+1] + 1):
                    s2[r][c] = s2[r-1][c+1] + 1
                if s2[r][c] > 0: max_len = max(max_len, s2[r][c])

                prev_co = s3_co[r-1][c+1] if r > 0 and c < m - 1 else 0
                prev_ce = s3_ce[r-1][c+1] if r > 0 and c < m - 1 else 0
                if grid[r][c] == 0: s3_ce[r][c] = 1 + prev_co
                if grid[r][c] == 2: s3_co[r][c] = 1 + prev_ce

        # Pass 2: Bottom-to-Top passes
        for r in range(n - 1, -1, -1):
            # Forward C pass for s3 (BL->TR) and s2_cont (TR->BL)
            for c in range(m):
                if grid[r][c] == 1:
                    s3[r][c] = 1
                elif r < n - 1 and c > 0 and s3[r+1][c-1] > 0 and grid[r][c] == get_expected(s3[r+1][c-1] + 1):
                    s3[r][c] = s3[r+1][c-1] + 1
                if s3[r][c] > 0: max_len = max(max_len, s3[r][c])
                
                prev_co = s2_co[r+1][c-1] if r < n - 1 and c > 0 else 0
                prev_ce = s2_ce[r+1][c-1] if r < n - 1 and c > 0 else 0
                if grid[r][c] == 0: s2_ce[r][c] = 1 + prev_co
                if grid[r][c] == 2: s2_co[r][c] = 1 + prev_ce

            # Backward C pass for s4 (BR->TL) and s1_cont (TL->BR)
            for c in range(m - 1, -1, -1):
                if grid[r][c] == 1:
                    s4[r][c] = 1
                elif r < n - 1 and c < m - 1 and s4[r+1][c+1] > 0 and grid[r][c] == get_expected(s4[r+1][c+1] + 1):
                    s4[r][c] = s4[r+1][c+1] + 1
                if s4[r][c] > 0: max_len = max(max_len, s4[r][c])
                
                prev_co = s1_co[r+1][c+1] if r < n - 1 and c < m - 1 else 0
                prev_ce = s1_ce[r+1][c+1] if r < n - 1 and c < m - 1 else 0
                if grid[r][c] == 0: s1_ce[r][c] = 1 + prev_co
                if grid[r][c] == 2: s1_co[r][c] = 1 + prev_ce
        
        # Pass 3: Combine at turning points
        for r in range(n):
            for c in range(m):
                # Turn s1 (+1,+1) -> s2 (+1,-1). Next cell: (r+1, c-1)
                l1 = s1[r][c]
                if l1 > 0 and r + 1 < n and c - 1 >= 0:
                    l2 = s2_co[r+1][c-1] if l1 % 2 != 0 else s2_ce[r+1][c-1]
                    max_len = max(max_len, l1 + l2)

                # Turn s2 (+1,-1) -> s4 (-1,-1). Next cell: (r-1, c-1)
                l1 = s2[r][c]
                if l1 > 0 and r - 1 >= 0 and c - 1 >= 0:
                    l2 = s4_co[r-1][c-1] if l1 % 2 != 0 else s4_ce[r-1][c-1]
                    max_len = max(max_len, l1 + l2)
                
                # Turn s3 (-1,+1) -> s1 (+1,+1). Next cell: (r+1, c+1)
                l1 = s3[r][c]
                if l1 > 0 and r + 1 < n and c + 1 < m:
                    l2 = s1_co[r+1][c+1] if l1 % 2 != 0 else s1_ce[r+1][c+1]
                    max_len = max(max_len, l1 + l2)

                # Turn s4 (-1,-1) -> s3 (-1,+1). Next cell: (r-1, c+1)
                l1 = s4[r][c]
                if l1 > 0 and r - 1 >= 0 and c + 1 < m:
                    l2 = s3_co[r-1][c+1] if l1 % 2 != 0 else s3_ce[r-1][c+1]
                    max_len = max(max_len, l1 + l2)
        
        return max_len