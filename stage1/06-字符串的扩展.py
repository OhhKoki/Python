# 1）字符串的三种定义方式
var01 = 'hellow world'
var02 = "hellow world"
var03 = """ hellow 
    world
    nihao
    shijie
"""

# 在字符串中使用单引号
var04 = "'hello world'"

# 在字符串中使用双引号
var05 = '"hello world"'

# 可以使用 \ 对单引号或者双引号进行转译
var06 = "\"hello world\""
var07 = '\'hello world\''

# 2）字符串的拼接
var08 = "hello"
var09 = "world"
var10 = 18287839851
print(var08 + var09)
# print(var08 + var09 + var10)    # 使用 + 进行拼接字符串时，拼接的对象必须都是字符串

"""
    3）字符串格式化方式一
        格式化符号：
            %d：将内容转换成整数，放入占位位置
            %f：将内容转换成浮点数数，放入占位位置
            %s：将内容转换成字符串，放入占位位置；
"""
var11 = "terry"
var12 = 20
var13 = 50.5
var14 = "姓名：%s" % var11
print(var14)
var15 = "姓名：%s，年龄：%d，体重：%f" % (var11, var12, var13)
print(var15)

# 字符串格式化方式二
var16 = f"姓名：{var11}，年龄：{var12}，体重：{var13}"
print(var16)

"""
    4）字符串格式化过程中对数字精度的控制
        精度控制的语法：m.n
            1）m 和 n 都可省略；
            2）如果 m 比数字本身宽度还小，则 m 不生效；
            3）使用 .n 对小数部分做精度限制时，会对小数进行四舍五入；
        例如：%5d、%5.2f、%.2f
"""
var17 = 12
var18 = 12.345
print("对 var17 宽度限制为 5，结果为：%5d" % var17)
print("对 var17 宽度限制为 1，结果为：%1d" % var17)
print("对 var18 宽度限制为 7，小数精度限制为 2，结果为：%7.2f" % var18)
print("对 var18 宽度不限制，小数精度限制为 2，结果为：%.2f" % var18)

# 表达式的格式化
print("2 ** 2 的结果为：%d" % (2 ** 2))
print(f"3 ** 3 的结果为：{3 ** 3}")


