"""
    1、在 Python 中构造方法的名称统一使用 __init__

    2、构造方法的作用：
        01）在创建类对象的时候，会自动执行；
        02）在创建类对象的时候，如果携带了参数，那么将传入的实参自动传递给 __init__ 方法使用；
"""


class Student:
    name = None
    age = None
    gender = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("Student init")


stu = Student("terry", 20, "man")
print(f"姓名：{stu.name}，年龄：{stu.age}，性别：{stu.gender}")