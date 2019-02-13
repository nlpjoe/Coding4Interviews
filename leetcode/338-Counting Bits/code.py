class Solution1(object):
    '''暴力法O(n*size(n))'''
    def countBits(self, num):
        return [self.nBits(i) for i in range(num+1)]

    def nBits(self, num):
        cnt = 0
        while num:
            num &= (num-1)
            cnt += 1
        return cnt

print(Solution1().countBits(3))

class Solution(object):
    def countBits(self, num):
        dp = [0] * (num+1)
        for i in range(num+1):
            dp[i] = dp[i>>1] + i%2
        return dp

print(Solution().countBits(3))