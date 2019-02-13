class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        dp = [[0]*len(A[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i == 0:
                    dp[i][j] = A[i][j]
                else:
                    dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i-1][max(0, j-1)], dp[i-1][min(j+1, len(A[0])-1)])
        return min(dp[len(A)-1])

print(Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))