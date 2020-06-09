# 算法思路： 统计每个字符出现次数， 找出所有出现次数等于1的字符，组成res。 然后返回第一个出现的位置



# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dic = {}
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        res = []
        for x, y in dic.items():
            if y == 1:
                res.append(x)
        if not res:
            return -1
        for i in range(len(s)): 
            if s[i] in res:
                return i