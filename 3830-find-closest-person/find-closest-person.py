class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        # def negate(x):
        #     if x<0:
        #         return +x

        if abs(z-x) < abs(z-y):
            return 1
        elif abs(z-x) == abs(z-y):
            return 0
        else:
            return 2
        