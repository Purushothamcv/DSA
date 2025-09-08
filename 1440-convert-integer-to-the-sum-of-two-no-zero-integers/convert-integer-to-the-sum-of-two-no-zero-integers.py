class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """ 
        # a=[]
        def isnozero(x):
            return 0 if '0' in str(x) else 1
        for i in range(1,n):
            x=n-i
            if isnozero(i) and isnozero(x):
                return [i,x]

        