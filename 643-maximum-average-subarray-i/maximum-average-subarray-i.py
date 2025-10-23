class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n=len(nums)
        if n<k:
            return None
        summ=0
        # n=len(nums)
        for i in range(k):
            summ+=nums[i]
        summavg=summ/float(k)
        maxavg=summavg
        for i in range(k,n):
            sumwin=summ+nums[i]-nums[i-k]
            summ=sumwin
            sumwinavg=sumwin/float(k)
            if sumwinavg>maxavg:
                maxavg=sumwinavg
        return maxavg        