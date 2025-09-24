class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
    
        res = []
        
        # If the result is negative
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Integer part
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        if remainder == 0:
            return "".join(res)
        
        res.append(".")
        
        # Dictionary to store seen remainders
        seen = {}
        
        while remainder != 0:
            if remainder in seen:
                # Insert parentheses
                res.insert(seen[remainder], "(")
                res.append(")")
                break
            
            seen[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(res)
            