"""
    1、类的定义语法为：
        class 类名:
            成员变量
            成员方法

    2、创建类对象的方式：
        对象名 = 类名称()
"""


# 定义类
class Student:
    name = None
    age = None
    gender = None


# 创建对象
stu = Student()

# 给对象属性赋值
stu.name = "Terry"
stu.age = 20
stu.gender = "man"

# 获取对象的信息
print(f"姓名为：{stu.name}，年龄为：{stu.age}，性别为：{stu.gender}")