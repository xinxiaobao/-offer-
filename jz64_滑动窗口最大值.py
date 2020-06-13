# 算法思路： 用列表切片，用max函数求出每一段的最大值，添加到res中， 返回res


class Solution:
    def maxInWindows(self, num, size):
        # write code here
        length = len(num)
        if not num or not size or size > length:
            return []
        res = []
        for i in range(length - size + 1):
            res.append(max(num[i: i+size]))
        return res