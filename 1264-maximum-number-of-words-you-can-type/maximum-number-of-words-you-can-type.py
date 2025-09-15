class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)
    
        count = 0
        for word in text.split():
        # If no broken letter is in the word, we can type it
            if not (set(word) & broken):
                count += 1
        return count
            

