class Solution(object):
    def readBinaryWatch(self, turnedOn):
        result = []
        
        for hour in range(12):        # 0 to 11
            for minute in range(60):  # 0 to 59
                
                # Count total 1 bits
                if (bin(hour).count('1') + bin(minute).count('1')) == turnedOn:
                    
                    # Format minute with 2 digits
                    time = str(hour) + ":" + format(minute, "02d")
                    result.append(time)
        
        return result
