class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=bin(n)[2:].zfill(32)
        x=m[::-1]
        result=0
        for digit in x:
            result=result*2+int(digit)
        return result
        # return m