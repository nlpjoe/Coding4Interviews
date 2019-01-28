class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        n = list(range(n))
        if not n: return -1
        i = 0
        while len(n) != 1:
            for _ in range(m-1):
                i += 1
                i %= len(n)
            n.pop(i)
        return n

print(Solution().LastRemaining_Solution(5, 3))