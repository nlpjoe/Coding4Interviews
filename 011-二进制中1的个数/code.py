from ctypes import *
def NumberOf1(n):
    # write code here
    cnt = 0
    while c_int(n).value:
        n = n & (n-1)
        cnt += 1
        print(c_int(n), n)
    return cnt

print(NumberOf1(-3))




# # -*- coding:utf-8 -*-
# class Solution:
#     def NumberOf1(self, n):
#         # write code here
#         return bin(n).replace("0b","").count("1") if n>=0 else bin(2**32+n).replace("0b","").count("1")
