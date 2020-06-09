
# 算法思路： 如果 k大于 tinput的长度，返回空值； 用sort函数对输入排序，用列表切片输出

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        tinput.sort(reverse=False)
        return tinput[:k]
        
        
sol = Solution()
tinput = [4,5,1,6,2,7,3,8]
k = 4
print(sol.GetLeastNumbers_Solution(tinput, k))