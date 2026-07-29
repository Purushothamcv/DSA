class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        max_area=0
        l=0
        r=n-1
        while l<r:
            area=(r-l)*min(height[l],height[r])
            if area>max_area:
                max_area=max(area,max_area)
            elif height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area


        


        