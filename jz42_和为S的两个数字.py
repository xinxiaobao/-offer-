# 算法思路： 数组是有序，可以用双指针，small 和 big 从两头逼近，大于就见效big指针，小于就增加small指针， 
#           相等时，比较是否乘积最小，最小，保留这两个数


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        n = len(array)
        small, big = 0, n-1
        multy_min = float('inf')
        m, n = None, None
        while small < big:
            if array[small] + array[big] == tsum:
                if array[small] * array[big] < multy_min:
                    m, n = array[small], array[big]
                    multy_min = array[small] * array[big]
                small += 1
            elif array[small] + array[big] < tsum:
                small += 1
            else:
                big -= 1
        if not m and not n:
            return []
        return m, n

array, tsum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],21
sol = Solution()
print(sol.FindNumbersWithSum(array, tsum))