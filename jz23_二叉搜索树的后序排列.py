'''
二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树：
 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。
    ---- 引用百度百科
 '''
# 算法思路：后序最后一个值为根，小于根，都是左子树，右子树必须都大于根，否则不是二叉搜索树
#         然后递归求左子树和右字数，最后得到二叉树是否为二叉搜索树的


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        
        root = sequence[-1]
        for i in range(len(sequence)):
            if root < sequence[i]:
                break
        for j in range(i, len(sequence)-1):
            if root > sequence[j]:
                return False
        left, right = True, True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        if i < len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right

sequence = [4,8,6,12,16,14,10]
sol = Solution()
print(sol.VerifySquenceOfBST(sequence))