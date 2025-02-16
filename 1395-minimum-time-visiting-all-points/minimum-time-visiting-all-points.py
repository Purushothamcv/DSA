class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x1,y1=points.pop()
        result=0
        while points:
            x2,y2=points.pop()
            a=y2-y1
            b=x2-x1
            result+=max(abs(a),abs(b))
            x1,y1=x2,y2
        return result
        