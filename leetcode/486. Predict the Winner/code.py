class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for d in range(1, n):
            for i in range(n-d):
                dp[i][i+d] = max(nums[i] - dp[i+1][i+d], nums[i+d] - dp[i][i+d-1])
        return dp[0][n-1] >= 0

print(Solution().PredictTheWinner([1, 5, 233, 7]))