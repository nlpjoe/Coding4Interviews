def jumpFloorII(number):
    # write code here
    f1 = 1
    if number == 1: return f1
    for _ in range(number-1):
        f1 = 2*f1
    return f1
    