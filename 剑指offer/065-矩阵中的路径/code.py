# -*- coding:utf-8 -*-
def DFS(matrix, row, col, path, visited):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or (row, col) in visited: 
        return False
    if path[0] == matrix[row][col]:
        if len(path) == 1:
            return True
        return DFS(matrix, row+1, col, path[1:], visited| {(row, col)}) or \
            DFS(matrix, row-1, col, path[1:], visited| {(row, col)}) or \
            DFS(matrix, row, col-1, path[1:], visited| {(row, col)}) or \
            DFS(matrix, row, col+1, path[1:], visited| {(row, col)})

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        array = list(matrix)
        array = [array[i*cols:(i+1)*cols] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                visited = set()
                if DFS(array, i, j, list(path), visited): 
                    return True
        return False

print(Solution().hasPath("ABCESFCSADEE",3,4,"BCCED"))
print(Solution().hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS",5,8,"SLHECCEIDEJFGGFIE"))
print(Solution().hasPath("AAAAAAAAAAAA",3,4,"AAAAAAAAAAAA"))

