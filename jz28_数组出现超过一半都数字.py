# 算法思路： 统计数组每个数字出现频率，组成字典； 取字典的值最大，如果超过数组长度一半
#           则返回该字典的值，否则返回0

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        dic = {}
        for i in numbers:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        dic_max = max(dic.values())
        dic_max_key = list(dic.keys())[list(dic.values()).index(dic_max)]
        return dic_max_key if 2*dic_max > len(numbers) else 0

numbers = [4,2,1,4,2,4]
sol = Solution()
print(sol.MoreThanHalfNum_Solution(numbers))