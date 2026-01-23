import heapq

class Solution(object):
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        # Doubly linked list using indices
        left = [-1] + list(range(n - 1))
        right = list(range(1, n)) + [-1]
        alive = [True] * n

        # Min-heap of (pair_sum, index)
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        # Count initial inversions
        inv = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                inv += 1

        cnt = 0

        while inv > 0:
            # Get a valid minimum adjacent pair
            while True:
                pair_sum, i = heapq.heappop(heap)
                j = right[i]
                if j != -1 and alive[i] and alive[j] and nums[i] + nums[j] == pair_sum:
                    break

            # Remove old inversions
            if left[i] != -1 and nums[left[i]] > nums[i]:
                inv -= 1
            if nums[i] > nums[j]:
                inv -= 1
            if right[j] != -1 and nums[j] > nums[right[j]]:
                inv -= 1

            # Merge i and j
            nums[i] = pair_sum
            alive[j] = False

            r = right[j]
            right[i] = r
            if r != -1:
                left[r] = i

            # Add new inversions
            if left[i] != -1 and nums[left[i]] > nums[i]:
                inv += 1
            if r != -1 and nums[i] > nums[r]:
                inv += 1

            # Push new adjacent sums
            if r != -1:
                heapq.heappush(heap, (nums[i] + nums[r], i))
            if left[i] != -1:
                heapq.heappush(heap, (nums[left[i]] + nums[i], left[i]))

            cnt += 1

        return cnt
