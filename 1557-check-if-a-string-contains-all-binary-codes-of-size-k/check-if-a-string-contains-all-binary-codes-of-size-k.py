class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        
        # If total possible substrings < 2^k, impossible
        if n - k + 1 < (1 << k):
            return False
        
        seen = set()
        
        for i in range(n - k + 1):
            seen.add(s[i:i+k])
            
            # Early stopping (optimization)
            if len(seen) == (1 << k):
                return True
        
        return len(seen) == (1 << k)