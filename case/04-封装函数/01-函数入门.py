"""
    函数的语法：
        def 函数名(形参):
            函数体
            return 返回值
"""


# 1）函数的使用案例
def add(x, y):
    return x + y


var01 = add(2, 3)
print(var01)


# 注意！！！无返回值的函数，实际上会返回一个 None 值，类型为：<class 'NoneType'>
# 即：函数不管是否有 return 操作，都会返回值（没有 return 操作就返回一个 None）
# 这个 None 在 if 或者 while 语句中视为 False !!!
def say_hi():
    # 不使用 return 进行返回时，函数会返回 None
    print("hi")


var02 = say_hi()
var03 = type(var02)
print(var02)
print(var03)


# None 使用案例
def check_age(age):
    if age > 18:
        return "success"
    else:
        return None


var04 = check_age(17)
if not var04:
    print("未成年")

var05 = None


# 2）函数说明文档：在函数体中使用多行注释 """ 即可自动生成格式，然后自行补充即可
def sum_number(num1, num2):
    """
    函数可以接收两个参数，然后进行两数进行相加并返回
    :param num1: 加数
    :param num2: 被加数
    :return:     两数相加的结果
    """
    return num1 + num2


# 3）在方法外定义的变量为全局变量，在方法内定义的为局部变量。使用 global 关键字可以在方法内声明一个变量为全局变量
var06 = 100
var07 = 200


def change():
    var06 = 101
    global var07
    var07 = 201


change()
print(var06)
print(var07)
