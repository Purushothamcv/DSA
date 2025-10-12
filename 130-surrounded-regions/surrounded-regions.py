class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None
        """
        if not board:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            # Stop if out of bounds or not 'O'
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            # Temporarily mark as 'T' (safe zone)
            board[r][c] = 'T'
            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Mark all border-connected 'O's as safe ('T')
        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows - 1] or c in [0, cols - 1]) and board[r][c] == 'O':
                    dfs(r, c)

        # Step 2: Flip all remaining 'O' → 'X', and 'T' → 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
