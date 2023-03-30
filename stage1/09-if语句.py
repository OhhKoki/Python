"""
    1）if 语句
        if 条件1:
            条件1成立时执行的代码
        elif 条件2:
            条件2成立时执行的代码
        elif 条件N:
            条件N成立时执行的代码
        else
            所有条件都不满足时执行的代码
"""
age = 17

if age > 18:
    print("年龄小于18")
elif age < 18:
    print("年龄小于18")
else:
    print("年龄等于18")