from ctypes import *

class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            temp = c_int(num1 ^ num2).value  # 不带进位的相加结果
            num2 = c_int((num1 & num2) << 1).value  # 带进位
            num1 = temp
        return num1

print(Solution().Add(-1, 23))

