# 找规律
# 1， 2， 4， 8， 16
# 2^(n-1)



class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number-1)