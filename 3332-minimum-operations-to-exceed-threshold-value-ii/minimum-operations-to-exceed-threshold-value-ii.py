class Solution(object):
    def heapify_up(self, heap, index):
        while index > 0:
            parent = (index - 1) // 2
            if heap[parent] > heap[index]:
                heap[parent], heap[index] = heap[index], heap[parent]
                index = parent
            else:
                break

    def heapify_down(self, heap, index):
        size = len(heap)
        while 2 * index + 1 < size:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2
            
            if left < size and heap[left] < heap[smallest]:
                smallest = left
            if right < size and heap[right] < heap[smallest]:
                smallest = right
            
            if smallest == index:
                break
            
            heap[index], heap[smallest] = heap[smallest], heap[index]
            index = smallest

    def heappush(self, heap, value):
        heap.append(value)
        self.heapify_up(heap, len(heap) - 1)

    def heappop(self, heap):
        if len(heap) == 1:
            return heap.pop()
        root = heap[0]
        heap[0] = heap.pop()
        self.heapify_down(heap, 0)
        return root

    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = nums[:]
        heap.sort()
        operations = 0
        
        while len(heap) > 1 and heap[0] < k:
            x = self.heappop(heap)
            y = self.heappop(heap)
            new_value = min(x, y) * 2 + max(x, y)
            self.heappush(heap, new_value)
            operations += 1
        
        return operations if heap[0] >= k else -1
