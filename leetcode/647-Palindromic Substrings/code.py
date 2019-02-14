class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for d in range(1, n):
            for i in range(n-d):
                if d == 1:
                    dp[i][i+d] = s[i] == s[i+d]
                else:
                    dp[i][i+d] = dp[i+1][i+d-1] and s[i] == s[i+d]
        cnt = 0
        for col in dp:
            for row in col:
                if row: cnt += 1
        return cnt

print(Solution().countSubstrings('aaa'))