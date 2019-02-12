
#  234 345
#  233445
def MergeElem(data, start, mid, end, temp):  # data[start...mid], data[mid+1...end]
    cnt = 0
    i = start
    j = mid + 1
    k = start
    while i <= mid and j <= end:
        if data[j] < data[i]:  # data[start...i...mid] data[mid+1...j...end]
            temp[k] = data[j]
            cnt += j - k
            j += 1
            k += 1
        else:
            temp[k] = data[i]
            i += 1
            k += 1
    while i <= mid:
        temp[k] = data[i]
        i += 1
        k += 1
    while j <= end:
        temp[k] = data[j]
        j += 1
        k += 1
    data[start:end+1] = temp[start:end+1]
    return cnt

def InverseCore(data, start, end, temp):
    cnt = 0
    if start < end:
        mid = (start + end) // 2
        cnt += InverseCore(data, start, mid, temp)
        cnt += InverseCore(data, mid+1, end, temp)
        cnt += MergeElem(data, start, mid, end, temp)
    return cnt

def InversePairs(data):
    # write code here
    temp = data[:]
    count = InverseCore(data, 0, len(data)-1, temp)
    return count

print(InversePairs([1,2,3,5,4,6,7,0]))