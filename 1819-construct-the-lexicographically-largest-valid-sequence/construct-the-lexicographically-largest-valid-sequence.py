class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        size = 2 * n - 1
        result = [0] * size
        used = set()
        
        def backtrack(index):
            if index == size:
                return True
            if result[index] != 0:
                return backtrack(index + 1)
            
            for num in range(n, 0, -1):  # Start from largest number
                if num in used:
                    continue
                
                if num == 1:
                    result[index] = num
                    used.add(num)
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    used.remove(num)
                else:
                    if index + num < size and result[index + num] == 0:
                        result[index] = result[index + num] = num
                        used.add(num)
                        if backtrack(index + 1):
                            return True
                        result[index] = result[index + num] = 0
                        used.remove(num)
            
            return False
        
        backtrack(0)
        return result