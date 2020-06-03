# 0, 1, 1, 2, 3, 5, ...

class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        pre = 0
        current = 1
        for i in range(n-1):
            current, pre = pre+current, current
        return current

# print(Fibonacci(3))