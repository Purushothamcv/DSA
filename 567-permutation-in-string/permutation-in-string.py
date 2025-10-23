class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        
        # Step 1: Build frequency map for s1
        freq1 = {}
        for ch in s1:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1

        # Step 2: Initialize frequency map for the first window in s2
        freq2 = {}
        for i in range(len1):
            ch = s2[i]
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1

        # Step 3: Slide the window across s2
        for i in range(len2 - len1):
            if freq1 == freq2:
                return True

            # Character going out of the window
            left_char = s2[i]
            freq2[left_char] -= 1
            if freq2[left_char] == 0:
                del freq2[left_char]

            # Character coming into the window
            right_char = s2[i + len1]
            if right_char in freq2:
                freq2[right_char] += 1
            else:
                freq2[right_char] = 1

        # Check the last window
        return freq1 == freq2
