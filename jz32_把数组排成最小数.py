# 算法思路： 判断a, b 的前后位置，通过比较 ab, ba; ab > ba,则b应该在a前面
#          然后用冒泡排序，对所有进来两两比较排序


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        num_str = list(map(str, numbers))
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if int(num_str[i]+num_str[j]) > int(num_str[j] + num_str[i]):
                    num_str[i], num_str[j] = num_str[j], num_str[i]

        return ''.join(num_str)