class Solution:
    def StrToInt(self, s):
        # write code here
        res = 0
        flag = 1
        for i in range(len(s)):
            if i == 0 and s[i] == '+':
                continue
            elif i == 0 and s[i] == '-':
                flag = -1
                continue
            n = ord(s[i]) - ord('0')
            if n>=0 and n<=9:
                res = 10 * res + n
            else:
                return False
        return res * flag

print(Solution().StrToInt('-1234'))
