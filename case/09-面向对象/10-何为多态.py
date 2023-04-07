"""
    1、什么是多态？
        同一个行为，使用不同的对象获得不同的状态，这就是多态！

        以父类做声明定义，以子类做实际工作，用以获得同一行为的不同状态;

        这种设计的思想就是：
            父类来确定有哪些方法，具体的方法实现，由子类类自行决定；
            这种写法，称为抽象类，或者接口；

    2、什么抽象类？
        含有抽象方法的类称为抽象类

        什么是抽象方法？
            方法体是空实现（pass）的方法称为抽象方法

    3、抽象类的作用？
        多用于顶层设计（设计标准），以便子类做具体的实现，也是对子类的一种软约束，要求子类必须复写父类的一些方法
"""


class Animal:
    def speak(self):
        # 含有 pass 的方法称为抽象方法，含有抽象方法的类称为抽象类
        pass


class Dog:
    def speak(self):
        print("汪汪汪")


class Cat:
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


# 多态演示
dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)