# 如果root只有一个点，直接返回root
# root 的左右交换
# 左右分别又进行交换，迭代下去
# 最后返回root树

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root