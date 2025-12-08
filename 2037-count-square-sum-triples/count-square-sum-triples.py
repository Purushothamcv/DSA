class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        a={}
        for i in range(1,n+1):
            a[i*i]=i
        count = 0 
        for i in range(1,n+1):
            for j in range(1,n+1):
                z=(i*i + j*j)
                if z in a:
                    y=a[z]
                    if y<=n:
                        count+=1
        return count







        
        