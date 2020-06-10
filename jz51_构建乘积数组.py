# 算法思路： 暴力解题，时间复杂度为 O（n^2）


# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        res = []
        length = len(A)
        for i in range(length):
            temp = 1
            for j in range(length):
                if i != j:
                    temp *= A[j]
            res.append(temp)
        return res