class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        count=0
        if not s:
            return 0
        i=n-1
        while i>=0 and s[i] == ' ':
            i-=1
        
        while i>=0 and s[i]!=" ":
                count+=1
                i-=1
        
            
        return count

        