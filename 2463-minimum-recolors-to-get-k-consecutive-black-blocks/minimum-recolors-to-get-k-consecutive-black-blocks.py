class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        white_count = blocks[:k].count('W')
        min_changes = white_count

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                white_count -= 1
            if blocks[i] == 'W':
                white_count += 1

            min_changes = min(min_changes, white_count)

        return min_changes


            
            