class Solution(object):
    def maxProfit1(self, prices):
        # 超时算法
        res = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                res = max(prices[j] - prices[i], res)
        return res

    def maxProfit(self, prices):
        # 零维动态规划
        if not prices: return 0
        dp = prices[0]
        res = 0
        for i in range(len(prices)):
            res = max(prices[i] - dp, res)
            dp = min(dp, prices[i])
        return res

print(Solution().maxProfit([7,1,5,3,6,4]))
        