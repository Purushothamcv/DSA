class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)  # recursive call
        result = ""
        count = 1
        
        # run-length encode the previous term
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result += str(count) + prev[i - 1]
                count = 1
        
        # add the last group
        result += str(count) + prev[-1]
        
        return result


# # Example usage:
# sol = Solution()
# print(sol.countAndSay(4))  # Output: "1211"
# print(sol.countAndSay(1))  # Output: "1"
