# 算法思路： 丑数 = (2^p2) * (3^p3) * (5^p5), 
#           每次循环，取2*res[p2], 3*res[p3], 5*res[p5]最小值，
#           加入res列表，直到res长度到了index，返回最后一个值



class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 1:
            return index
        res = [1]
        p2, p3, p5 = 0, 0, 0
        while len(res) < index:
            temp = min(2*res[p2], 3*res[p3], 5*res[p5])
            if temp == 2*res[p2]:
                p2 += 1
            if temp == 3*res[p3]:
                p3 += 1
            if temp == 5*res[p5]:
                p5 += 1
            res.append(temp)
        return res[-1]

