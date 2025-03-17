class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen=0
        n=len(s)
        
        for i in range(n):
            hashi={}
            for j in range(i,n):
                if hashi.get(s[j],0)==1:
                    break
                length=j-i+1
                maxlen=max(length,maxlen)
                hashi[s[j]]=1

        return maxlen
                
            

            