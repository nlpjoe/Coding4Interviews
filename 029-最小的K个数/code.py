
def sink(array, k):
    n = len(array)
    left = 2 * k + 1
    right = 2 * k + 2
    if left >= n: return
    min_i = left 
    if right < n and array[left] > array[right]:
        min_i = right
    if array[min_i] < array[k]:
        array[min_i], array[k] = array[k], array[min_i]
        sink(array, min_i)

def build_heap(list):
    n = len(list)
    for i in range(n//2, -1, -1):
        sink(list, i)

    return list

def GetLeastNumbers_Solution(tinput, k):
    if k > len(tinput): return []
    heap = build_heap(tinput)  # 建堆o(n)复杂度
    res = []
    for _ in range(k):  # 取topk o(klogn)复杂度
        heap[0], heap[-1] = heap[-1], heap[0]
        res.append(heap.pop())
        sink(heap, 0)
    return res


print(GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4))