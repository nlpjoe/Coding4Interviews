def sum(n):
    try:
        1 % n
        return n + sum(n-1)
    except:
        return 0


class Solution:
    def Sum_Solution(self, n):
        return sum(n)


print(Solution().Sum_Solution(10))