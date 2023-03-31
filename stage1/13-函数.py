"""
    函数的语法：
        def 函数名(形参):
            函数体
            return 返回值
"""


# 函数的使用案例
def add(x, y):
    return x + y


var01 = add(2, 3)
print(var01)


# 注意！！！无返回值的函数，实际上会返回一个 None 值，类型为：<class 'NoneType'>
# 即：函数不管是否有 return 操作，都会返回值（没有 return 操作就返回一个 None）
# 这个 None 在 if 或者 while 语句中视为 False !!!
def say_hi():
    print("hi")


var02 = say_hi()
var03 = type(var02)
print(var02)
print(var03)


# None 在 if 语句的使用案例
def check_age(age):
    if age > 18:
        return "success"
    else:
        return None


var04 = check_age(17)
if not var04:
    print("未成年")
