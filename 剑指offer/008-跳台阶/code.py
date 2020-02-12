class Solution(object):
    def numWays(self, n):
        if n == 0: return 1
        f1 = 1
        f2 = 2
        if n == 1: return f1
        if n == 2: return f2
        for _ in range(n-2):
            f2, f1 = f1+f2, f2
        return f2 % 1000000007
