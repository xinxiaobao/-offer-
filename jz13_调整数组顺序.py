# 调整数组顺序使奇数在前，偶数在后
# 算法逻辑，奇数按顺序放在一个数组中，偶数也按顺序放在一个数组中
#  奇数数组+偶数数组，输出， 即为答案

class Solution:
    def reOrderArray(self, array):
        # write code here
        res1 = []
        res2 = []
        for num in array:
            if num % 2 == 1:
                res1.append(num)
            else:
                res2.append(num)
        return res1 + res2