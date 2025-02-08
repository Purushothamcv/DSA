class NumberContainers(object):

    def __init__(self):
        # Maps each index to the current number stored at that index.
        self.index_map = {}
        # Maps each number to a sorted list of indices where that number appears.
        self.number_map = {}

    def _find_insert_position(self, lst, target):
        """
        Helper function that returns the index at which 'target' should be inserted 
        in 'lst' (which is already sorted) to maintain the sorted order.
        """
        left, right = 0, len(lst)
        while left < right:
            mid = (left + right) // 2
            if lst[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def change(self, index, number):
        """
        Inserts or replaces the number at the given index.
        If there is already a number at that index, remove the old entry before adding the new one.
        
        :param index: int - the index in the container.
        :param number: int - the number to store at the given index.
        :rtype: None
        """
        # If the index already holds a number, remove it from the corresponding sorted list.
        if index in self.index_map:
            old_number = self.index_map[index]
            if old_number in self.number_map:
                # Remove the index from the list.
                # Using list.remove() here to remove the first occurrence.
                try:
                    self.number_map[old_number].remove(index)
                except ValueError:
                    pass  # In case the index is not in the list (should not happen).
        
        # Update the index_map with the new number.
        self.index_map[index] = number
        
        # Insert the index into the sorted list for the new number.
        if number not in self.number_map:
            self.number_map[number] = [index]
        else:
            pos = self._find_insert_position(self.number_map[number], index)
            self.number_map[number].insert(pos, index)

    def find(self, number):
        """
        Returns the smallest index where the given number is stored.
        If no such index exists, returns -1.
        
        :param number: int - the number to look for.
        :rtype: int
        """
        if number not in self.number_map or len(self.number_map[number]) == 0:
            return -1
        return self.number_map[number][0]


# ---------------------------
# Example usage:
