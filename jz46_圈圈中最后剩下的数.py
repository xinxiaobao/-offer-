# 算法思路： 模拟整个过程，即可得出结果 ----方法一
#           方法二： f(n)=(f(n-1)+m)%n； 当n=1,f(1)=0;

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not n:
            return -1
        if n == 1:
            return 0
        nums = list(range(n))
        start = 0
        while len(nums) >= 2:
            length = len(nums)
            if m+start >= length:
                start = (start+m-1)%length
            else:
                start += (m-1)
            nums.pop(start)
        return nums[0]

# class Solution:
#     def LastRemaining_Solution(self, n, m):
#         # write code here
#         if not n or m < 1:
#             return -1
#         if n == 1:
#             return 0
#         res = 0
#         for i in range(2, n+1):
#             res = (res + m) % i
#         return res
n, m = 5,2
sol = Solution()
print(sol.LastRemaining_Solution(n, m))