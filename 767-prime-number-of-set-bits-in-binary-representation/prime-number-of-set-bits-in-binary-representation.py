class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def isprime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        count1=0
        for i in range(left,right+1):
            j=bin(i)[2:]
            count=0
            for k in range(len(j)):
                if j[k] == '1':
                    count+=1
            if isprime(count):
                count1+=1
        return count1

        