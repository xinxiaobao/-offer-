# 算法思路： 每次路径增加一个点，直到，到根结点，expectNumber是否为0，不是则返回上一个点，重新选择

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return self.res
        self.path.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and not root.left and not root.right:
            temp = self.path[:]
            self.res.append(temp)
        self.FindPath(root.left, expectNumber)
        self.FindPath(root.right, expectNumber)
        self.path.pop()
        return self.res

  
