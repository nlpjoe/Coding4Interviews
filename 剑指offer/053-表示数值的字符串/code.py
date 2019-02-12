class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        sign, point, hasE = False, False, False
        for i in range(len(s)):
            if s[i].lower() == 'e':
                if hasE: return False
                if i == len(s)-1: return False
                hasE = True
            elif s[i] == '+' or s[i] == '-':
                if sign and s[i-1].lower() != 'e': return False
                if not sign and i > 0 and s[i-1].lower() != 'e': return False
                sign = True
            elif s[i] == '.':
                if hasE or point: return False
                point = True
            elif ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
                return False
        return True