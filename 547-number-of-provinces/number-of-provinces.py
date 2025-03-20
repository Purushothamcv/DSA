class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        adj=[]
        count=0
        n=len(isConnected)
        for i in range(n):
            adj.append([])
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)

        vis=[0]*len(adj)
        for i in range(n):
            if vis[i]==0:
                count+=1
                self.dfs(i,vis,adj)
        return count
    def dfs(self,node,vis,adj):
        vis[node]=1
        for edges in adj[node]:
            if not vis[edges]:
                self.dfs(edges,vis,adj)
    





        