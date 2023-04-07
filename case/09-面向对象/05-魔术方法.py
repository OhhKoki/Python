"""
    1、什么是魔术方法？
        Python 对于类提供了许多内置方法，这些内置方法有其独特的作用，对于内置方法一般也称为：魔术方法；

        类似于 Java 中所有 Object 是所有类的父类，所有所有类中都包含 Object 中的方法！！！

    2、有那些常见的魔术方法？
        __init__：构造方法
        __str__：字符串方法（类似于 Java 的 toString() 方法）
        __lt__：小于、大于符号比较（类似于 Java 的 equals() 方法）
        __le__：小于等于、大于等于符号比较（类似于 Java 的 equals() 方法）
        __eq__：==符号比较（类似于 Java 的 equals() 方法）

"""


class Student:
    # 如果使用了构造方法，那么成员属性甚至可以不定义，离谱
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"name = {self.name}，age = {self.age}，gender = {self.gender}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


terry = Student("terry", 20, "man")
print(terry)

jerry = Student("jerry", 20, "man")
print(jerry)

# 通过 __lt__ 比较两个对象的大小
print(f"terry < jerry：{terry < jerry}")

# 通过 __le__ 比较两个对象的大小
print(f"terry <= jerry：{terry <= jerry}")

# 通过 __eq__ 比较两个对象的大小
print(f"terry == jerry：{terry == jerry}")

