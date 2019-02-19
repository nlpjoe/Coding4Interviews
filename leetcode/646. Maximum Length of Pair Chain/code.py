class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda d:d[0])
        n = len(pairs)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
        return dp[n-1]


class Solution1(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda d:d[1])
        res = 0
        cur = float('-inf')
        for p in pairs:
            if cur < p[0]:
                res += 1
                cur = p[1]
        return res

print(Solution().findLongestChain([[2, 3],[1,2], [4, 5]]))