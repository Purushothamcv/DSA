class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        n=len(height)
        right=n-1
        maxarea=0
        while left<=right:
            width=right-left
            minheight=min(height[left],height[right])
            area=width*minheight
            maxarea=max(maxarea,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea

        