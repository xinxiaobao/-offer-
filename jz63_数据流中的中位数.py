# 算法思路： 存入数据，排序一下， 数据长度为奇数，返回第 (length-1)//2 个 数， 
#          数据长度为偶数， 返回中间两个数的平均值


class Solution:
    def __init__(self):
        self.lis = []
    def Insert(self, num):
        self.lis.append(num)
        self.lis.sort()
        # write code here
    def GetMedian(self, num):
        # write code here
        length = len(self.lis)
        if length % 2 == 1:
            return self.lis[(length-1)//2]
        else:
            return (self.lis[length//2] + self.lis[length//2 -1])/2.0