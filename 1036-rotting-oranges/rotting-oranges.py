class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        queue = []
        fresh = 0
        
        # Step 1: Add all rotten oranges to queue and count fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                elif grid[i][j] == 1:
                    fresh += 1
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0
        index = 0  # for simulating queue pop from front
        
        # Step 2: BFS
        while index < len(queue):
            i, j, minutes = queue[index]
            index += 1
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2  # rot the orange
                    fresh -= 1
                    queue.append((ni, nj, minutes + 1))
        
        # Step 3: Check if any fresh oranges left
        return minutes if fresh == 0 else -1
