


# 25 % 时间复制度O(n^2), 数字太大就算不了
class Solution:
    def InversePairs(self, data):
        # write code here
        res = 0
        length = len(data)
        for i in range(length-1):
            for j in range(i, length):
                if data[i] > data[j]:
                    res += 1
        if res < 1000000007:
            return res
        return res%1000000007

    # 方法二，50%
    def InversePairs1(self, data):
        # write code here
        res = 0
        copy = data[:]
        copy.sort()
        for i in range(len(data)):
            index = data.index(copy[i])
            res += index
            data.pop(index)
        if res < 1000000007:
            return res
        return res%1000000007