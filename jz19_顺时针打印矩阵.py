# 用魔方翻转的思想， 
'''
例如 
1 2 3
4 5 6
7 8 9
输出并删除第一行后，再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可。
'''


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        while matrix and matrix[0]:
            res.extend(matrix.pop(0))
            matrix = self.turn(matrix)
        return res
    
    def turn(self, matrix):
        if not matrix:
            return matrix
        row = len(matrix)
        column = len(matrix[0])
        matrix_new = []
        for i in range(column-1, -1, -1):
            matrix_temp = []
            for j in range(row):
                matrix_temp.append(matrix[j][i])
            matrix_new.append(matrix_temp)
        return matrix_new