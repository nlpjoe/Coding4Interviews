class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10: n = 10
        res = 0
        f1 = 10
        f2 = 9*9
        if n == 0: return 1
        for i in range(1, n+1):
            if i == 1:
                res += f1
            elif i == 2:
                res += f2
            else:
                f2 = f2 * (11-i)
                res += f2
        return res

print(Solution().countNumbersWithUniqueDigits(2))

