class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # def anagram(i,j,words):
        #     for i in :
        if not words:
            return []

        result = [words[0]]  # always keep the first word

        for i in range(1, len(words)):
        # compare current word with the last word in result
            if sorted(words[i]) != sorted(result[-1]):
                result.append(words[i])

        return result