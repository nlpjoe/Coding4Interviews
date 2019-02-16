class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        T_ik0, T_ik1 = 0, float('-inf')
        T_ik0_pre = 0

        for p in prices:
            T_ik0_old= T_ik0
            T_ik0 = max(T_ik0, T_ik1 + p)
            T_ik1 = max(T_ik1, T_ik0_pre - p)
            T_ik0_pre = T_ik0_old
        return T_ik0
            


print(Solution().maxProfit([1,2,3,0,2]))


