class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total_drunk = numBottles
        empty = numBottles

        # While you have enough empty bottles to exchange
        while empty >= numExchange:
            # Exchange empty bottles for new full ones
            new_full = empty // numExchange
            total_drunk += new_full
            # Update empty bottles: remaining + newly emptied
            empty = (empty % numExchange) + new_full

        return total_drunk
            




        