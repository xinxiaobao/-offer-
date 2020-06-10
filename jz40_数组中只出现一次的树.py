
# 方法1： 用队列思想，每次取出一个数字，如果数组中还有这个数字，则不是要找的，把数组放到队尾，直到两个数字都被找到
# 方法2: 队列排序，用指针，当前位置不等于前一位，不等于后一位，则为我们要找到数字

# 29 ms  方法1
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        time = 0
        res = []
        while time <= 1:
            temp = array.pop(0)
            if temp not in array:
                res.append(temp)
                time += 1
            else:
                array.append(temp)
        return res

# 21 ms 方法2
class Solution2:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        array.sort()
        time = 0
        res = []
        print(array)
        if array[0] != array[1]:
            res.append(array[0])
            time += 1
        for i in range(1, len(array)-1):
            if (array[i-1] != array[i]) and (array[i] != array[i+1]):
                res.append(array[i])
                time += 1
            if time == 2:
                break
        if time == 1:
            res.append(array[-1])
        return res


array = [2,4,3,6,3,2,5,5]
sol = Solution()
print(sol.FindNumsAppearOnce(array))