class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        minlen=len(strs[0])
        for s in strs:
            if len(s)<minlen:
                minlen=len(s)
        prefix=""
        for i in range(minlen):
            character=strs[0][i]
            for s in strs[1:len(strs)]:
                if s[i]!=character:
                    return prefix
            prefix+=character
        return prefix



        