class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=right=0
        n=len(s)
        h={}
        maxlen=0
        for right in range(n):
            if s[right]  in h and h[s[right]]>=left:
                left=h[s[right]]+1
            h[s[right]]=right
            maxlen=max(maxlen,right-left+1)
        return maxlen
                
            

            