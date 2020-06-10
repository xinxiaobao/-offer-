# 平衡树指的是，任意节点的子树的高度差都小于等于1 (引用百度百科)
# 算法思路： 先写一个求深度的函数，再对每一个节点判断，看该节点的左子树的深度和右子树的深度的差是否大于1


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if abs(self.Max_Depth(pRoot.left) - self.Max_Depth(pRoot.right)) > 1:
            return False
        res = self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        return res
    
    def Max_Depth(self, root):
        if not root:
            return 0
        max_depth = max(self.Max_Depth(root.left), self.Max_Depth(root.right)) + 1
        return max_depth