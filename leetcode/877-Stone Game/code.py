class Solution(object):
    def stoneGame(self, piles):
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for d in range(1, n):       # 步宽
            for i in range(n-d):
                dp[i][i+d] = max(piles[i]-dp[i+1][i+d], piles[i+d]-dp[i][i+d-1])
        return dp[0][len(piles)-1] > 0

print(Solution().stoneGame([5,3,4,5]))

        