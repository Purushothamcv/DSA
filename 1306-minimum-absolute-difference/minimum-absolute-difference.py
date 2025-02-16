class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        n=len(arr)
        a=[]
        min=float('inf')
        for i in range(1,n):
            x=arr[i]-arr[i-1]
            if abs(x)<min:
                min=abs(x)
        for i in range(1,n):
            if arr[i]-arr[i-1]==min:
                a.append([arr[i-1],arr[i]])
        return a

        