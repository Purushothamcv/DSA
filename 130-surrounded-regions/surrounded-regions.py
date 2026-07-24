class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        if not board:
            return

        m = len(board)
        n = len(board[0])

        def dfs(r, c):

            # Boundary check
            if r < 0 or c < 0 or r >= m or c >= n:
                return

            # Stop if it is not O
            if board[r][c] != "O":
                return

            # Mark boundary-connected O as safe
            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Check left and right boundaries
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)

            if board[i][n - 1] == "O":
                dfs(i, n - 1)

        # Check top and bottom boundaries
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)

            if board[m - 1][j] == "O":
                dfs(m - 1, j)

        # Convert cells
        for i in range(m):
            for j in range(n):

                # Surrounded O
                if board[i][j] == "O":
                    board[i][j] = "X"

                # Safe O
                elif board[i][j] == "T":
                    board[i][j] = "O"