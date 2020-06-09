




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