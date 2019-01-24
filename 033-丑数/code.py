# 1 2 3 4 5 6 8

# def is_ugly(n):
#     while n % 2 == 0:
#         n /= 2
#     while n % 3 == 0:
#         n /= 3
#     while n % 5 == 0:
#         n /= 5
#     return n == 1

# 2345
def GetUglyNumber_Solution(index):
    # write code here
    if index <= 0: return 0
    uglys = set([1, 2, 3, 4, 5])
    cnt = 0
    i = 0
    while cnt < index:
        i += 1
        if i==1 or i / 2 in uglys or i/3 in uglys or i/5 in uglys:
            cnt += 1
            uglys.add(i)
        
    return i

print(GetUglyNumber_Solution(7))
