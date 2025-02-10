class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        
        while True:
            found=False
            for i in range(len(s)):
                if s[i].isdigit():
                    s.pop(i)
                    if i>0:
                        s.pop(i-1)
                    found=True
                    break
            if not found:
                break
            
        return "".join(s)

                
        

        