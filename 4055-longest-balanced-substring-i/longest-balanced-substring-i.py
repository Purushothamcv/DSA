class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_len = 0
        
        for i in range(n):
            freq = {}
            
            for j in range(i, n):
                # Update frequency
                freq[s[j]] = freq.get(s[j], 0) + 1
                
                values = freq.values()
                
                # Check if all frequencies are equal
                if max(values) == min(values):
                    max_len = max(max_len, j - i + 1)
        
        return max_len
