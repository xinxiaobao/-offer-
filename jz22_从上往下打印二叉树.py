# 算法思路，广度优先搜索，用队列实现先后顺序
# 把二叉树拿出来，取出根结点后，将左右结点放在队列后面
# 循环即可实现广度优先搜索

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = []
        res = []
        queue.append(root)
        
        while len(queue) > 0:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res