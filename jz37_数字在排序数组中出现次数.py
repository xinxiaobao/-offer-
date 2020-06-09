

class Solution:
    # 算法时间复杂度为O(n)
    def GetNumberOfK(self, data, k):
        # write code here
        res = 0
        for i in data:
            if i == k:
                res += 1
        return res

    def GetNumberOfK1(self, data, k):
        # write code here
        return data.count(k)