class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        n = len(s)
        for i in range(n):
            odd_s = self.palindromeAt(s, i, i)
            even_s = self.palindromeAt(s, i-1, i)
            res = max(res, odd_s, even_s, key=len)
        return res

    def palindromeAt(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

print(Solution().longestPalindrome('caba'))

