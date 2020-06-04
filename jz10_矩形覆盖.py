# 斐波那契数列
# 1， 2， 3， 5， 8， 13

class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 3:
            return number
        pre, current = 1, 2
        for i in range(number-2):
            pre,  current = current, pre+current
        return current