class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return None
        dic = {}
        for num in numbers:
            if num in dic and num != 0:

                return False
            elif num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        if 0 in dic:
            num_0 = dic.pop(0)
            length = len(dic) + num_0
            num_max, num_min = max(dic.keys()), min(dic.keys())
            return True if num_max - num_min < length else False
        else:
            length = len(dic)
            num_max, num_min = max(dic.keys()), min(dic.keys())
            return True if num_max - num_min < length else False


numbers = [1,3,0,5,0]
sol = Solution()
print(sol.IsContinuous(numbers))