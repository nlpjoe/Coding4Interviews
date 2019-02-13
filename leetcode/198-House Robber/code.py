class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        dp = [0] * (len(nums)+1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[len(nums)-1]

print(Solution().rob([1,2,1,3]))
print(Solution().rob([2,7,9,3,1]))
print(Solution().rob([0,0]))