class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a={}
        x=[]
        n=len(nums)
        for i in nums:
            a[i]=a.get(i,0)+1
        for key,value in a.items():
            if value>(n/3):
                x.append(key)
        return x
        