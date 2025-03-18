class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        count=0
        a={'a':0,'b':0,'c':0}
        for right in range(len(s)):
            a[s[right]]+=1
            while a['a']>0 and a['b']>0 and a['c']>0:
                count+=(len(s)-right)
                a[s[left]]-=1
                left+=1
        return count