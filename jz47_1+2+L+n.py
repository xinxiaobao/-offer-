'''
 # and中含0，返回0； 均为非0时，返回后一个值， 
2 and 0   # 返回0
2 and 1   # 返回1
1 and 2   # 返回2

# or中， 至少有一个非0时，返回第一个非0,
2 or 0   # 返回2
2 or 1   # 返回2
0 or 1   # 返回1 
'''
# 算法思路，运用递归，当n == 0 时，返回0； 用and代替判断语句
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and (n + self.Sum_Solution(n-1))