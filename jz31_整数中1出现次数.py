# 算法思路： 将所以数字变成字符串，并相加，用python 的字符串内置函数，count数出‘1’的数量

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        data = ''
        for i in range(1, n+1):
            data += str(i)
        return data.count('1')

