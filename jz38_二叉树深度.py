# 算法思路： 递归调用， 递归结束条件： 根结点为空，返回0。 二叉树的深度，可以变成求左右子树的深度，
#           取最大值加根节点，即加1。 使用递归调用自身，求的结果

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        
        count = max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) +1
        return count