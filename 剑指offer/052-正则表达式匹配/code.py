    

class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        s = '^' + s 
        pattern = '^' + pattern
        i = len(s) - 1
        j = len(pattern) - 1
        star_match = False
        while i>=0 and j>=0:
            if star_match:
                if pattern[j] == '.' or pattern[j] == s[i]:
                    if self.match(s[1:i], pattern[1:j]):  # 先靠前匹配，从1开始是去掉index为0的^
                        return True
                    else:
                        i -= 1
                else:
                    j -= 1
                    star_match = False
            else:
                if s[i] == pattern[j] or pattern[j] == '.':
                    i -= 1
                    j -= 1
                elif pattern[j] == '*':
                    star_match = True
                    j -= 1
                else:
                    return False
        return (i == -1 and j == -1)


print(Solution().match('aa', 'a*'))