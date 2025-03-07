class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """


        def simple_sieve(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False  
            for i in range(2, int(sqrt(limit)) + 1):
                if is_prime[i]:
                    for j in range(i * i, limit + 1, i):
                        is_prime[j] = False
            return [i for i in range(limit + 1) if is_prime[i]]

        if left < 2:
            left = 2

        limit = int(sqrt(right)) + 1
        small_primes = simple_sieve(limit)

        is_prime = [True] * (right - left + 1)
        for p in small_primes:
            start = max(p * p, (left + p - 1) // p * p)
            for j in range(start, right + 1, p):
                is_prime[j - left] = False

        primes = [i for i in range(left, right + 1) if is_prime[i - left]]

        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        closest_pair = [-1, -1]
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes[i], primes[i + 1]]

        return closest_pair