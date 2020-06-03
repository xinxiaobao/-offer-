def replace_space(s):
    #  replace 不能直接改变原来变量，需要重新赋值
    s = s.replace(' ', '%20')
    return s

s = 'We Are Happy'
print(replace_space(s))