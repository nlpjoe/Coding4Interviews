class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        t_ik0 = 0
        t_ik1 = float('-inf')
        for p in prices:
            t_ik0_old = t_ik0
            t_ik0 = max(t_ik0, t_ik1 + p)  #r or sell
            t_ik1 = max(t_ik1, t_ik0_old - p)  # r or buy
        return t_ik0
