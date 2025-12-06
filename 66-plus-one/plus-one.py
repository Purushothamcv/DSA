class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x = []
        n = len(digits)

        # If last digit is 9 → we must handle carry
        if digits[n-1] == 9:
            carry = 1
            for i in range(n-1, -1, -1):
                value = digits[i] + carry
                x.append(value % 10)
                carry = value // 10

            if carry > 0:
                x.append(carry)

            x.reverse()
            return x

        else:
            # Normal case (no carry needed)
            for i in range(n-1):
                x.append(digits[i])
            x.append(digits[n-1] + 1)
            return x