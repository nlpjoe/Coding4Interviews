def biSearch(data, k):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] > k:
            high = mid - 1
        elif data[mid] < k:
            low = mid + 1
    return high

def GetNumberOfK(data, k):
    # write code here
    if not data: return 0
    return biSearch(data, k+0.5) - biSearch(data, k-0.5)

print(GetNumberOfK([3,3,3, 4],3))
