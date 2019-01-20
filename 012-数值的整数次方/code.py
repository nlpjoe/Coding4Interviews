
def Power(base, exponent):
    # write code here
    if exponent == 0: return 1
    flag = 1
    if exponent < 0:
        exponent *= -1
        flag = 0
    temp = base
    res = 1
    while(exponent):
        if exponent & 1:
            res *= temp
        temp *= temp
        exponent = exponent >> 1

    return res if flag else 1.0/res

print(Power(2, 1))