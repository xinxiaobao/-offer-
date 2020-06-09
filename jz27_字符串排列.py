# 算法思路： 运动迭代思想，字符串，从头开始，每次固定一个字母，把其他所有可能情况都加进来，
#         固定字母，剩下字符串，用同样方法，不断迭代，直到 字符串小于等于1


# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) <= 1:
            return ss
        res = set()
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i]+ ss[i+1:]):
                res.add(ss[i]+j)
        return sorted(res)