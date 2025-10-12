class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        m=len(grid)
        n=len(grid[0])
        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return
            count=0
            grid[i][j]=0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(m):
            for j in range(n):
                if (i in [0,m-1] or j in [0,n-1] and grid[i][j] == 1):
                    dfs(i,j)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count+=1
        return count



        