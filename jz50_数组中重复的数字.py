# 记得看清题目说明，赋值和返回什么

# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        dic = {}
        for num in numbers:
            if num in dic:
                duplication[0] = num
                return True
            else:
                dic[num] = 1
        return False