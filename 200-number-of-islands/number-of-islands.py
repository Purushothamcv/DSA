class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count=0
        m=len(grid)
        n=len(grid[0])
        visited=[[0]*n for _ in range(m)]
        m=len(grid)
        n=len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n:
                return 
            if grid[r][c]=="0" or visited[r][c]:
                return
            visited[r][c]=1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=="1":
                    dfs(i,j)
                    count+=1
        return count