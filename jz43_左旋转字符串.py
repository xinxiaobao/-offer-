# 算法思路： 如果 n < len(s), 则返回 s[n:]+s[:n];
#            如果 n > len(s), 则先用n 除以 len(s) 取商， 再返回 s[new_n:] + s[:new_n]

class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ''
        length = len(s)
        if n < length:
            return s[n:] + s[:n]
        if n >= length:
            new_n = n % length
            return s[new_n:] + s[:new_n]