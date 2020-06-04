# 正数：原码 = 反码 = 补码
# 负数：反码-符号位不变，其他取反； 补码 = 反码+1
# 补码也等于 2^n + 负数

class Solution:
    def NumberOf1(self, n):
        # write code here
        if n >= 0:
            return bin(n).count('1')
        if n < 0:
            num = 2**32 + num
            return bin(num).count('1')
