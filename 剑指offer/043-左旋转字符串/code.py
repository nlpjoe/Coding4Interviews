def reverse(str, s, e):
    e -= 1
    while s < e:
        str[s], str[e] = str[e], str[s]
        s += 1
        e -= 1

class Solution:

    def LeftRotateString(self, s, n):
        # write code here
        if len(s) == 0 or n == 0: return s
        s = list(s)
        reverse(s, 0, n)
        reverse(s, n, len(s))
        reverse(s, 0, len(s))
        return ''.join(s)

print(Solution().LeftRotateString('abcdef', 3))


        