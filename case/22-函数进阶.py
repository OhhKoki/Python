"""
    1、函数存在多个返回值：
        01）语法形式：
            def 方法名():
                return 返回值1, 返回值2

            x, y = 方法名()

        02）细节说明：
            1、函数可以返回多个返回值，各个返回值之间使用逗号隔开即可；
            2、支持多种类型同时返回
            3、接收返回值时，按照返回值的的数量和顺序，定义对应数量的变量接收即可；

    2、函数的多种参数
        01）位置参数

        02）关键字参数

        03）不定长参数

        04）缺省参数

    3、函数作为参数传递
        def fun06(compute):
            result = compute(1, 2)
            print(result)

        def fun07(x, y):
            return x + y

        fun06(fun07)

    4、匿名函数
        01）使用 def 关键字可以定义带有名称的函数，例如：def fun01()


        02）使用 lambda 关键字可以定义匿名函数（匿名函数只能写一行），例如：
            def fun06(compute):
                result = compute(1, 2)
                print(result)

            fun06(lambda x, y: x + y)

        03）有名函数和匿名函数的区别：有名称的函数通过函数名可以重复使用，而匿名函数只能临时使用一次

"""


# 函数多返回值
def fun01():
    return "terry", 20, 50.5, True


var01, var02, var03, var04 = fun01()
print(f"var01 的值为：{var01}，var02 的值为：{var02}，var03 的值为：{var03}， var04 的值为：{var04}")


"""
    函数的多种参数
        01）位置参数
    
        02）关键字参数
    
        03）不定长参数
    
        04）缺省参数
"""


# 定义带参的函数
def fun02(name, age, weight, gender):
    var05 = f"姓名：{name}，年龄：{age}，体重：{weight}，性别：{gender}"
    return var05


# 位置参数
var06 = fun02("张三", 20, 50.5, "男")
print(f"使用位置参数的形式调用函数，函数的返回结果为：{var06}")

# 关键字参数
# 注意：对于关键字参数来说，参数顺序无所谓
# 注意：使用关键字参数时，可以同时使用位置参数，但是位置参数必须是首位开始且有序
var07 = fun02("李四", 21, weight=60.5, gender="男")
print(f"使用关键字参数的形式调用函数，函数的返回结果为：{var07}")


# 定义不定长参数 -- 位置不定长
def fun03(*args):
    print(f"位置不定长参数的的使用，args 的类型为：{type(args)}，参数的内容为：{args}")


# 使用不定长参数 -- 位置不定长
fun03("terry", 20, 50.5, "man")


# 定义不定长参数 -- 关键字不定长
def fun04(**kwargs):
    print(f"关键字不定长参数的的使用，kwargs 的类型为：{type(kwargs)}，参数的内容为：{kwargs}")


# 使用不定长参数 -- 关键字不定长
fun04(name="terry", age=20, weight=55.5, gender="man")


# 定义带默认值的函数
def fun05(name, age, weight=70.5, gender="男"):
    var05 = f"姓名：{name}，年龄：{age}，体重：{weight}，性别：{gender}"
    return var05


# 注意：对于缺省参数必须从右到左依次定义
var08 = fun05("王五", age="22")
print(f"使用带缺省参数的函数，函数的返回结果为：{var08}")


# 函数作为参数传递
def fun06(compute):
    result = compute(1, 2)
    print(f"参数 compute 的类型为：{type(compute)}，compute 函数的运行结果为：{result}")


def fun07(x, y):
    return x + y


fun06(fun07)


# 匿名函数
def fun08(compute):
    result = compute(1, 2)
    print(f"参数 compute 的类型为：{type(compute)}，compute 函数的运行结果为：{result}")


fun08(lambda x, y: x * y)

