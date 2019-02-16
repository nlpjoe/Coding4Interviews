class Solution(object):
    def maxProfit(self, k, prices):
        n = len(prices)
        if k >= n>>1:
            k = n>>1
        T_ik0 = [0] * (k+1)
        T_ik1 = [float('-inf')] * (k+1)
        for p in prices:
            for d in range(1, k+1):
                T_ik0[d] = max(T_ik0[d], T_ik1[d] + p)
                T_ik1[d] = max(T_ik1[d], T_ik0[d-1] - p)
        return T_ik0[k]

print(Solution().maxProfit(k=2, prices=[3,2,6,5,0,3]))