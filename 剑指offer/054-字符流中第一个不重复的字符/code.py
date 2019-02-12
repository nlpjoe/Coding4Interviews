class Solution:
    # 返回对应char
    def __init__(self):
        self.data = []
    def FirstAppearingOnce(self):
        # write code here
        return self.data[0] if self.data else '#'
    def Insert(self, char):
        # write code here
        n = len(self.data)
        for i in range(n-1, -1, -1):
            if self.data[i] == char:
                self.data.pop(i)
                return
        self.data.append(char)


s = Solution()
print(s.Insert('g'))
print(s.Insert('o'))
print(s.Insert('o'))
print(s.Insert('g'))
print(s.Insert('l'))
print(s.Insert('e'))