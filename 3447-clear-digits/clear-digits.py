class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)  # Convert string to a list for easy modification
    
        while True:
            found = False  # Flag to check if we removed a digit
            for i in range(len(s)):
                if s[i].isdigit():
                    # Remove the digit
                    s.pop(i)
                    # Remove the closest non-digit character to its left
                    if i > 0:
                        s.pop(i - 1)
                    found = True  # Mark that we removed a digit
                    break  # Restart the loop after modification
            if not found:
                break  # Stop when no more digits are found

        return "".join(s)  # Convert list back to string
            

            