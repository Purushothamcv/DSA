class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        count=0
        visited=[0]*n
        # node=0
        def dfs(node):
            visited[node]=1
            for i in range(n):
                if isConnected[node][i]==1 and visited[i]==0:
                    dfs(i)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count+=1
        return count





        