# 如果数组长度为0，输出0
# 否则输出数组的最小值，极为答案

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        else:
            return min(rotateArray)