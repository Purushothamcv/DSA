class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # maxarea=0
        # count=0
        m=len(image)
        n=len(image[0])
        # visited=[[0]*n for _ in range(m)]
        # m=len(grid)
        # n=len(grid[0])
        originalcolor=image[sr][sc]
        if color==originalcolor:
            return image
        def dfs(r,c):
            # count+=1
            if r<0 or c<0 or r>=m or c>=n:
                return 
            if image[r][c]!=originalcolor:
                return
            image[r][c]=color
            # visited[r][c]=1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        dfs(sr,sc)    
        return image
        # for i in range(m):
        #     for j in range(n):
        #         if not visited[i][j] and grid[i][j]==1:
        #             count+=1
        #             dfs(i,j)
                    
        # return count
        
        