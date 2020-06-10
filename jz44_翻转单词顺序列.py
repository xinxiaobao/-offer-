# 算法思路： 将用split（） 内置函数将字符串 s 分割成 列表， 然后将列表反转，加空格组成字符串输出；
#         注意： 当输入为一串空格时，’     ‘， 要求返回同样一串空格，不能返回空值

class Solution:
    def ReverseSentence(self, s):
        # write code here
        lis = s.split()
        if not len(lis):
            return s
        return ' '.join(lis[::-1])