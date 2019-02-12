class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        sum = res
        for i in range(1, len(nums)):
            if sum < 0:
                 sum = nums[i]
            else: 
                sum += nums[i]
            res = max(res, sum)
        return res

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([-2,1]))
