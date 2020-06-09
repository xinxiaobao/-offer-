# 算法思路： 运用动态规划， 以某个树结尾时，最大的值为 dp[i] = max{dp[i-1]+array[i], array[i]}
#           然后返回 dp列表最大值，即为连续子数组最大和

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        dp = array[:]
        for i in range(1, len(array)):
            dp[i] = max(dp[i-1]+array[i], array[i])
        return max(dp)