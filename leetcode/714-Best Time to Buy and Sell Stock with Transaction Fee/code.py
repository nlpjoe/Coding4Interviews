class Solution(object):
    def maxProfit(self, prices, fee):
        T_ik0 = 0
        T_ik1 = float('-inf')
        for p in prices:
            T_ik0_old = T_ik0
            T_ik0 = max(T_ik0, T_ik1 + p - fee)
            T_ik1 = max(T_ik1, T_ik0_old - p)
        return T_ik0


# print(Solution().maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2))
# print(Solution().maxProfit(prices = [9,8,7,1,2], fee = 3))
print(Solution().maxProfit(prices = [4,5,2,4,3,3,1,2,5,4], fee = 1))