class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n <= 1: return n
        dp = {}
        res = 0
        s = set(A)
        for i in range(n):
            for j in range(i):
                if A[i] - A[j] < A[j] and A[i] - A[j] in s:
                    dp[A[j], A[i]] = dp.get((A[i] - A[j], A[j]), 2) + 1
                    res = max(res, dp[A[j], A[i]])
        return res
        
print(Solution().lenLongestFibSubseq([2,4,7,8,9,10,14,15,18,23,32,50]))