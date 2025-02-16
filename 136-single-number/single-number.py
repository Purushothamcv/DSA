class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a={}
        for i in nums:
            a[i]=a.get(i,0)+1
        for i,value in a.items():
            if a[i]==1:
                return i
        
        