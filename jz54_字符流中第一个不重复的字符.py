# 算法思路： 用字符串count函数，filter函数，筛选出只出现一次的字符串，返回第一个字符即可

class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''

    def FirstAppearingOnce(self):
        # write code here
        res = list(filter(lambda  x: self.s.count(x) == 1, self.s))
        return res[0] if res else '#'

    def Insert(self, char):
        # write code here
        self.s += char

