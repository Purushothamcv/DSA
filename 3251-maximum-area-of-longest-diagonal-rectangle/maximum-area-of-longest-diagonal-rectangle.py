class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        maxx=float('-inf')
        # count=0
        # a=0
        # c=1
        # for _ in dimensions:
        #     count+=1
        d=0
        for i in dimensions:
            a=0
            c=1
            for j in i:
                a+=j*j
                c*=j
            b=a**0.5
            if b>maxx or (b == maxx and c > d):
                maxx=b
                d=c
        return d
        