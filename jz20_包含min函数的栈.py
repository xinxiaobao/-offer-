'''
思路：利用一个辅助栈来存放最小值,
    实现取最小值的算法时间复杂度为 O（1）

    栈  3，4，2，5，1
    辅助栈 3，3，2，2，1
'''


class Solution:
    def __init__(self):
        self.stack = []
        self.min_list = []
    def push(self, node):
        # write code here
        min_temp = self.min()
        if not min_temp or node < min_temp:
            self.min_list.append(node)
        else:
            self.min_list.append(min_temp)
        self.stack.append(node)
    def pop(self):
        # write code here
        if self.stack:
            self.stack.pop()
            self.min_list.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        if self.stack:
            return self.min_list[-1]