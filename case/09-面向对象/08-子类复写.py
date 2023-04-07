"""
    1、什么是复写
        子类继承父类的成员属性和成员方法后，如果对其不满意，可以进行复写，即：在子类中重新定义同名的属性或方法即可；

        如果想要使用被复写的父类成员或者方法，可以使用如下形式：
            01）父类名.成员变量
            02）父类名.成员方法(self)
            03）super().成员变量
            04）super().成员方法()
            05）只能在子类的内部调用父类的同名成员，子类的实体对象默认调用的是子类复写过的方法
"""


class Person:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"我是一个人，我的名字是：{self.name}，我的年龄是：{self.age}")


class Student(Person):
    gender = None

    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    # 方法复写
    def say_hi(self):
        super().say_hi()
        print(f"我是一个学生，我的名字是：{self.name}，我的年龄是：{self.age}，我的性别是：{self.gender}")


stu = Student("jerry", 20, "man")
stu.say_hi()


