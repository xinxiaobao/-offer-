# 算法思路： 用 内置float()函数，有点不够完美，有时间应该再回头钻研

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try: 
            digit = float(s)
            return True
        except:
            return False