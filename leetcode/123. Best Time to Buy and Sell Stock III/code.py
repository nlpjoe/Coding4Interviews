class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        T_i10, T_i11, T_i20, T_i21 = [float('-inf')] * 4
        for p in prices:
            T_i10_old = T_i10
            T_i10 = max(T_i10, T_i11 + p)
            T_i11 = max(T_i11, -p)
            T_i20 = max(T_i20, T_i21 + p)
            T_i21 = max(T_i21, T_i10_old - p)
        return max(T_i20, T_i10, 0)

print(Solution().maxProfit([3,3,5,0,0,3,1,4]))