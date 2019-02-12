def getN(i, j):
    res = 0
    while i:
        res += (i % 10)
        i //= 10
    while j:
        res += (j % 10)
        j //= 10
    return res

def DFS(array, i, j, threshold, visited):
    if i<0 or j<0 or i>len(array)-1 or j>len(array[0])-1 or array[i][j]>threshold or visited[i][j]:
        return 0
    res = 1
    visited[i][j] = 1
    res += DFS(array, i+1, j, threshold, visited)
    res += DFS(array, i-1, j, threshold, visited)
    res += DFS(array, i, j+1, threshold, visited)
    res += DFS(array, i, j-1, threshold, visited)
    return res

class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        array = []
        for i in range(rows):
            res = []
            for j in range(cols):
                res.append(getN(i, j))
            array.append(res)
        from pprint import pprint
        pprint(array)
        visited = [[0] * len(array[0]) for _ in range(len(array))]
        return DFS(array, 0, 0, threshold, visited)


