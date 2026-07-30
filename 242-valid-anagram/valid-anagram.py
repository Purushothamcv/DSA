class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a={}
        b={}
        for i in range(len(s)):
            a[s[i]]=a.get(s[i],0)+1
        for j in range(len(t)):
            b[t[j]]=b.get(t[j],0)+1
        # print(a)
        if a==b:
            return True
        else:
            return False
        