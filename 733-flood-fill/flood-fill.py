class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        # adj=[]
        # n=len(image)
        # for i in range(n):
        #     adj.append([])
        # for i in range(n):
        #     for j in range(n):
        #         if image[i][j]==1 and i!=j:
        #             adj[i].append(j)
        row=len(image)
        column=len(image[0])
        start_color=image[sr][sc]
        if image[sr][sc]==color:
            return image
        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>=column or image[i][j]!=start_color:
                return
            image[i][j]=color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        dfs(sr,sc)
        return image


                    
        

        