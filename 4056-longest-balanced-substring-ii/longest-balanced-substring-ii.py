class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0
        
        max_len = 0
        
        # --- CASE 1: Only 1 distinct character ---
        # Any substring of identical characters (like "aaaa") is balanced 
        # because the only distinct character 'a' appears X times.
        curr_streak = 0
        for i in range(n):
            if i > 0 and s[i] == s[i-1]:
                curr_streak += 1
            else:
                curr_streak = 1
            max_len = max(max_len, curr_streak)

        # --- CASE 2: Exactly 2 distinct characters ---
        for char1, char2 in [('a', 'b'), ('b', 'c'), ('a', 'c')]:
            last_seen = {0: -1}
            c1, c2 = 0, 0
            start_of_block = 0
            
            for i, char in enumerate(s):
                if char == char1:
                    c1 += 1
                elif char == char2:
                    c2 += 1
                else:
                    # Reset if the 3rd character breaks the window
                    last_seen = {0: i}
                    c1, c2 = 0, 0
                    continue
                
                diff = c1 - c2
                if diff in last_seen:
                    # We only care if BOTH characters exist in this specific substring
                    # to qualify for the "2 distinct characters" rule.
                    # Use a separate check to ensure diversity.
                    sub_len = i - last_seen[diff]
                    # Check if this range actually contains both chars
                    if c1 > 0 and c2 > 0:
                        max_len = max(max_len, sub_len)
                
                if diff not in last_seen:
                    last_seen[diff] = i

        # --- CASE 3: Exactly 3 distinct characters ---
        last_seen_triple = {(0, 0): -1}
        counts = {'a': 0, 'b': 0, 'c': 0}
        
        for i, char in enumerate(s):
            counts[char] += 1
            state = (counts['b'] - counts['a'], counts['c'] - counts['a'])
            
            if state in last_seen_triple:
                # Only update if all three characters have appeared at least once
                if counts['a'] > 0 and counts['b'] > 0 and counts['c'] > 0:
                    max_len = max(max_len, i - last_seen_triple[state])
            else:
                last_seen_triple[state] = i
                
        return max_len