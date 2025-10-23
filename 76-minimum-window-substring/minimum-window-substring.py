class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Step 1: Build frequency map of t manually
        need = {}
        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        # Step 2: Initialize window tracking
        window = {}
        have = 0
        need_count = len(need)
        res = ""
        res_len = float("inf")

        left = 0

        # Step 3: Expand the window
        for right in range(len(s)):
            c = s[right]
            if c in window:
                window[c] += 1
            else:
                window[c] = 1

            # Check if this char fulfills the required count
            if c in need and window[c] == need[c]:
                have += 1

            # Step 4: Contract from left when valid
            while have == need_count:
                # Update result if smaller window found
                window_size = right - left + 1
                if window_size < res_len:
                    res = s[left:right + 1]
                    res_len = window_size

                # Remove from left side
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1

        return res
