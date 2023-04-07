"""
    1、什么是类型注解？
        Python 在 3.5 版本的时候引入了类型注解，以方便静态类型检查工具对代码进行类型推断，然后进行提示；

    2、类型注解的语法是什么？
        变量:类型

    3、类型注解支持哪些类型？
        01）基础数据类型注解
        02）基础容器类型注解
        03）变量类型的注解
        04）方法形参类型注解
        05）方法返回值类型注解

    4、类型注解是提示性的，不是强制性的；例如标记了 int，然后使用 str 赋值也是不会报错的！！！

    5、Union 注解类型
        当我们对 tuple 和 dict 进行注解时，tuple 和 dict 可能存在多种类型，例如：
            var_13: tuple = ("terry", 20, 55.5)
            var_14: dict = {"name": "terry", "age": 18, "weight": 55.5}

        此时可以使用 Union 进行描述，例如：
            from typing import Union
            var_13: tuple[Union[str, int, float]] = ("terry", 20, 55.5)
            var_14: dict[str, Union[str, int, float]] = {"name": "terry", "age": 18, "weight": 55.5}
"""


# 1.1）基础数据类型注解--直接指定类型
var_01: str = "terry"
var_02: int = 20
var_03: float = 55.5
var_04: bool = True

# 1.2）基础数据类型注解--在注解中指定类型
var_01 = "terry"                    # type: str
var_02 = 20                         # type: int
var_03 = 55.5                       # type: float
var_04 = True                       # type: bool


# 2.1）基础容器类型注解--直接指定类型
var_05: list = [1, 2, 3]
var_06: tuple = (1, 2, 3)
var_07: set = {1, 2, 3}
var_08: dict = {"name": "terry"}

# 2.2）基础容器类型注解--在注解中指定类型
var_05 = [1, 2, 3]                  # type: list
var_06 = (1, 2, 3)                  # type: tuple
var_07 = {1, 2, 3}                  # type: set
var_08 = {"name": "terry"}          # type: dict


# 3.1）基础容器类型注解详细版本--直接指定类型
var_09: list[int] = [1, 2, 3]
var_10: tuple[str, int, float] = ("terry", 20, 55.5)
var_11: set[int] = {1, 2, 3}
var_12: dict[str, int] = {"age": 20}

# 3.2）基础容器类型注解详细版本--在注解中指定类型
var_09 = [1, 2, 3]                  # type: list[int]
var_10 = ("terry", 20, 55.5)        # type: tuple[str, int, float]
var_11 = {1, 2, 3}                  # type: set[int]
var_12 = {"age": 20}                # type: dict[str, int]


class Math:
    # 给方法的参数添加注解
    def add(self, x: int, y: int):
        return x + y

    # 给方法的返回值添加注解
    def sub(self, x: int, y: int) -> int:
        return x - y


# 给对象进行注解
math: Math = Math()
print(math.add(1, 2))
print(math.sub(3, 2))


# Union 类型
from typing import Union
var_13: tuple[Union[str, int, float]] = ("terry", 20, 55.5)
var_14: dict[str, Union[str, int, float]] = {"name": "terry", "age": 18, "weight": 55.5}


def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


print(add(1, 5.5))






