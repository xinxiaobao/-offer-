# 前序(根左右)，中序(左根右)，后序(左右根)
# 先序遍历特点：第一个值是根节点
# 中序遍历特点：根节点左边都是左子树，右边都是右子树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        index = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:index+1], tin[0:index])
        root.right = self.reConstructBinaryTree(pre[index+1:], tin[index+1:])
        return root

pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]

res = Solution()
root = res.reConstructBinaryTree(pre, tin)
print(root.val)
print(root)