"""
    1、类包含两个成员：成员变量 & 成员方法

    2、成员变量的定义方式：
        class 类名:
            变量名 = 变量值

    3、成员方法的定义方式：
        class 类名:
            def 方法名(self, 形参, 形参, ...):
                方法体

        可以看到，在方法的形参列表中，存在一个 self 关键字，self 关键字是成员方法定义时必须添加的
            01）它用于表示类对象自身的意思（相当于 this）；
            02）该关键字必须在形参的第一个位置；
            03）在方法内部，想要访问类的成员变量，必须使用 self；
            04）尽管在形参列表中存在 self，当我们使用类对象调用方法时，self 会自动被 Python 传入，
"""


class Student:
    name = None
    age = None
    gender = None

    def say_hi(self, msg):
        print(f"{msg}, my name is：{self.name}")


stu = Student()
stu.name = "terry"
stu.age = 20
stu.gender = "man"

stu.say_hi("nice to meet you")
