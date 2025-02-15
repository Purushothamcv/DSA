class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_valid_partition(num_str, target):
            length = len(num_str)
            for mask in range(1 << (length - 1)):  
                total = 0
                part = 0
                for i in range(length):
                    part = part * 10 + int(num_str[i])  
                    if (mask >> i) & 1 or i == length - 1:  
                        total += part
                        part = 0  
                if total == target:
                    return True
            return False

        total_punishment = sum(i * i for i in range(1, n + 1) 
        if is_valid_partition(str(i * i), i))
        return total_punishment