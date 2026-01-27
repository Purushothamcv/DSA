class Solution(object):
    def minCost(self, n, edges):
        import heapq

        out_edges = [[] for _ in range(n)]
        in_edges = [[] for _ in range(n)]

        for u, v, w in edges:
            out_edges[u].append((v, w))
            in_edges[v].append((u, w))

        INF = float('inf')
        dist = [[INF, INF] for _ in range(n)]
        dist[0][0] = 0

        # (cost, node, used_switch_at_this_node)
        pq = [(0, 0, 0)]

        while pq:
            cost, u, used = heapq.heappop(pq)

            if cost > dist[u][used]:
                continue

            if u == n - 1:
                return cost

            # 1️⃣ Normal outgoing edges
            for v, w in out_edges[u]:
                if cost + w < dist[v][0]:
                    dist[v][0] = cost + w
                    heapq.heappush(pq, (cost + w, v, 0))

            # 2️⃣ Reverse one incoming edge (only once at THIS node)
            if used == 0:
                for v, w in in_edges[u]:
                    if cost + 2 * w < dist[v][0]:
                        dist[v][0] = cost + 2 * w
                        heapq.heappush(pq, (cost + 2 * w, v, 0))

        return -1
