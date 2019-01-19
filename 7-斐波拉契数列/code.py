def Fibonacci(n):
    # write code here
    f1 = 0
    f2 = 1
    if n == 0: return f1
    elif n == 1: return f2
    for _ in range(n-1):
        f2, f1 = f1+f2, f2
    return f2
print(Fibonacci(3))