class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # count=0
        # for i in range(low,high+1):
        #     if (i%2)!=0:
        #         count+=1
        # return count                
        # count=0
        # while low<high+1:
        #     if (low%2)!=0:
        #         count+=1
        #     low+=1
        # return count
        if (low%2)!=0 or (high %2 )!=0:
            return ((high-low)//2)+1
        return (high-low)//2



        