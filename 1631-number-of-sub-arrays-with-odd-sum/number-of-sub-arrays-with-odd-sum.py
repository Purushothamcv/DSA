class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  # There's one even prefix sum (0)
        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num  # Update prefix sum
            
            if prefix_sum % 2 == 1:
                result += even_count  # Odd prefix sum pairs with previous even prefix sums
                odd_count += 1
            else:
                result += odd_count  # Even prefix sum pairs with previous odd prefix sums
                even_count += 1
            
            result %= MOD  # To prevent overflow
        
        return result

            