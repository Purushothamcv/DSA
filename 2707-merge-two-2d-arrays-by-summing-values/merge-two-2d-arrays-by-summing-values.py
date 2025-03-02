class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """

        n1 = len(nums1)
        n2 = len(nums2)
        a={}
        c=[]
        for i in range(n1):
            a[nums1[i][0]]=nums1[i][1]
        for i in range(n2):
            if nums2[i][0] in a:
                a[nums2[i][0]]=a[nums2[i][0]]+nums2[i][1]
            else:
                a[nums2[i][0]]=nums2[i][1]
        for key,val in sorted(a.items()):
            c.append([int(key),val])

        return c       



        