def partition(input, low, high):
    pivot = input[low]
    while low < high:
        while low < high and pivot <= input[high]:
            high -= 1
        input[low] = input[high]
        while low < high and pivot >= input[low]:
            low += 1
        input[high] = input[low]
    input[low] = pivot
    return low


def GetLeastNumbers_Solution(tinput, k):
    if k > len(tinput) or k <= 0: return []
    idx = partition(tinput, 0, len(tinput) - 1)
    low = 0
    high = len(tinput) - 1
    while idx != k - 1:
        if idx < k - 1:
            low = idx + 1
            idx = partition(tinput, low, high)
        if idx > k - 1:
            high = idx - 1
            idx = partition(tinput, low, high)
    return tinput[:k]


print(GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4))
print(GetLeastNumbers_Solution([-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8], 4))