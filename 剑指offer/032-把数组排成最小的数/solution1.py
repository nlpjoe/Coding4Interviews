def number_len(n):
    res = 0
    while n:
        n //= 10
        res += 1
    return res


def PrintMinNumber(numbers):
    # write code here
    if len(numbers) == 1: return numbers[0]
    max_len = number_len(max(numbers))
    map = {}
    for i in range(len(numbers)):
        n = numbers[i]
        pad = n % 10
        n_len = number_len(n)
        for j in range(max_len-n_len):
            n = n*10+pad
        map[n*10+n_len] = i
    keys = sorted(map.keys())
    res = numbers[map[keys[0]]]
    for i in range(1, len(keys)):
        n = numbers[map[keys[i]]]
        res = res * 10 ** number_len(n) + n
    return res



    # map = {numbers[i]:i for i in range(len(numbers))}

print(PrintMinNumber([11,1,111]))