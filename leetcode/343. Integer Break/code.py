class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        def max_n(n, i):
            if n % i == 0:
                return (n//i) ** i
            else:
                dn = (n // i + 1) * i - n
                return (n // i + 1) ** (i - dn) * (n // i) ** dn
        res = 1
        for i in range(2, n+1):
            res = max(res, max_n(n, i))
        return res


print(Solution().integerBreak(2))