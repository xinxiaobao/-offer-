# 尽可能用多用3, 不能被3整除，如果余数是2， 则变成 2*3*3...
# 如果余数是1，则变成 4*3*3...
def cut_rope(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    elif number % 3 == 0:
        res = 3**(number//3)
    elif number % 3 == 1:
        res = 4 * 3**((number-4)//3)
    else:
        res = 2 * 3**((number-2)//3)
    return res

print(cut_rope(9))