class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n=len(fruits)
        used=[False]*n
        count=0
        for i in fruits:
            # count=0
            placed=False
            for j in range(n):
                if not used[j] and baskets[j]>=i:
                    used[j]=True
                    placed=True
                    break
            if not placed:
                count+=1
        return count

                    
        