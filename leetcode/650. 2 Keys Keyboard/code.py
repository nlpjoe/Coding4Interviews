class Solution1(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        for i in range(2, n+1):
            for j in range(i//2, -1, -1):
                if i % j == 0:
                    dp[i] = dp[j] + i//j
                    break
        return dp[n]

class Solution2(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(2, n+1):
            while n % i == 0:
                res += i
                n /= i
        return res

print(Solution1().minSteps(24))

