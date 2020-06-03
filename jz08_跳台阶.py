# 符合斐波那契数列分布，做法同上一题，斐波那契数列算法

class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 2:
            return number
        pre = 1
        current = 2
        for i in range(number - 1):
            pre, current = current, pre+current
        return pre