def IsPopOrder(pushV, popV):
    # write code here
    stack = []
    i = 0
    for v in pushV:
        stack.append(v)
        while stack and stack[-1] == popV[i]:
            i += 1
            stack.pop(-1)
    if not stack:
        return True
    else:
        return False
    

print(IsPopOrder([1, 2, 3, 4, 5], [4,3,5,1,2]))