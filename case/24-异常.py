"""
    1、异常的捕获语法
        try:
            有可能出现异常的代码
        except [异常 as 别名:]
            出现异常后执行的代码
        [else:]
            没有异常时执行的代码
        [finally:]
            任何情况都执行的代码

    2、异常的传递性
"""


# 捕获所有的异常（不推荐）
try:
    var01 = 1 / 0
except:
    print("捕获全部异常：出现异常了")

# 捕获指定的异常
try:
    var01 = 1 / 0
except ZeroDivisionError as e:
    print(f"捕获指定异常：出现异常，异常信息为：{e}")

# 捕获多个的异常
try:
    var01 = 1 / 0
    # print(test)
except (ZeroDivisionError, NameError) as e:
    print(f"捕获多个异常：出现异常，异常信息为：{e}")

# 异常的完整结构
file = None
try:
    file = open("/Users/terry/Documents/Workspace/PythonProjects/Python/test.txt", "r", encoding="UTF-8")
    print(f"文件已存在，使用 r 模式打开文件")
except FileNotFoundError as e:
    file = open("/Users/terry/Documents/Workspace/PythonProjects/Python/test.txt", "w", encoding="UTF-8")
    print(f"文件不存在，使用 w 模式打开文件")
else:
    print(f"文件正常读取")
finally:
    print(f"关闭文件")
    file.close()

print("----------")


# 异常的传递性
def fun01():
    print("fun01 开始执行")
    num = 1 / 0
    print("fun01 结束执行")


def fun02():
    print("fun02 开始执行")
    fun01()
    print("fun02 结束执行")


def main():
    print("main 开始执行")
    try:
        fun02()
    except Exception as e:
        print(f"出现异常，异常信息为：{e}")
    print("main 结束执行")


main()
