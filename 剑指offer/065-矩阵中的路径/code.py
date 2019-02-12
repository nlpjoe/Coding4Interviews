# -*- coding:utf-8 -*-
def BFS(matrix, row, col, path, visited):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or visited[row][col]: 
        return False
    if path[0] == matrix[row][col]:
        if len(path) == 1:
            return True
        visited[row][col] = 1
        if BFS(matrix, row+1, col, path[1:], visited) or \
            BFS(matrix, row-1, col, path[1:], visited) or \
            BFS(matrix, row, col-1, path[1:], visited) or \
            BFS(matrix, row, col+1, path[1:], visited):
            return True
        return False
    else:
        return False
    
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        array = list(matrix)
        array = [array[i*cols:(i+1)*cols] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                visited = [[0] * len(array[0]) for _ in range(len(array))]
                if BFS(array, i, j, list(path), visited): 
                    return True
        return False

print(Solution().hasPath("ABCESFCSADEE",3,4,"BCCED"))
print(Solution().hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS",5,8,"SLHECCEIDEJFGGFIE"))
print(Solution().hasPath("AAAAAAAAAAAA",3,4,"AAAAAAAAAAAA"))

