class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x=bin(n)[2:]
        for i in range(len(x)-1):
            if x[i] == x[i+1]:
                return False
        return True 

        