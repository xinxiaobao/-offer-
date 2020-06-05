# 算法思路，将树结构转换成字符串，判断字符串是否包含另一个字符串，用 in 就可以了
# 当 pRoot2 是空时，返回False

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot2:
            return False
        def tree2str(tree):
            if tree:
                return str(tree.val) + tree2str(tree.left) +  tree2str(tree.right)
            else:
                return ''
        pRoot1_str = tree2str(pRoot1)
        pRoot2_str = tree2str(pRoot2)
        if pRoot2_str in pRoot1_str:
            return True
        else:
            return False