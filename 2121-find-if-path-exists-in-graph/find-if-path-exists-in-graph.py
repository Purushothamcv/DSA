class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph=[[]for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=[0]* len(graph)
        # node=0
        print(graph)
        def dfs(node):
            visited[node]=1
             
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        dfs(source)
        if visited[destination]==1:
            return True
        return False
    
    
        
                


    