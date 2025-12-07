class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a={}
        maxx=0
        maxi=0
        for i in nums:
            a[i]=a.get(i,0)+1
        for key,value in a.items():
            if value>maxi:
                maxi=value
                maxx=key
                
        return maxx


        
        
        