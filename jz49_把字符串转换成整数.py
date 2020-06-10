# 算法思路： 用python内置字符串判断函数，isdigit（） 当字符串带‘+’‘-’符号时，需要单独处理
#           不能用字符串转换成整数的库 -- 有待完善


class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        if s.isdigit():
            return int(s)
        elif s[0] in ['+', '-'] and s[1:].isdigit():
            return int(s)
        else:
            return 0




