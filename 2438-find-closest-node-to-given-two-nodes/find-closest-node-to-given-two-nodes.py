class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        
        n = len(edges)

        def get_distances(start):
            dist = [-1] * n
            d = 0
            while start != -1 and dist[start] == -1:
                dist[start] = d
                start = edges[start]
                d += 1
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        result = -1
        min_distance = float('inf')

        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_distance:
                    min_distance = max_dist
                    result = i
                elif max_dist == min_distance and i < result:
                    result = i

        return result

            