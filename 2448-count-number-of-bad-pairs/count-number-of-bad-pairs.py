class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        total_pairs=(n*(n-1))//2
        dict={}
        good_pairs=0
        for i in range(n):
            key=nums[i]-i
            if key in dict:
                good_pairs+=dict[key]
                dict[key]+=1
            else:
                dict[key]=1
        return total_pairs-good_pairs

        
        
        return bad_pairs