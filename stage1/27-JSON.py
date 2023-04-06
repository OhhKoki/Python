"""
    1、什么是 JSON
        01）JSON 是一种轻量级的数据交互格式。可以按照 JSON 指定的格式去组织和封装数据；
        02）JSON 本质上是一个带有特定格式的字符串；

    2、JSON 的功能
        01）JSON 就是一个在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互，类似于英语和普通话的作用；
        02）各种编程语言存储数据的容器不尽相同，例如在 Python 中有 dict ，而在 Java 中却是 Map，此时 JSON 可以作为各个言语间的通用数据格式；

    3、JSON 的格式和 Python 的 dict 一摸一样

    4、dict 和 JSON 相互转换
        01）json.dumps(JSON格式的数据)：将数据转为JSON；
        02）json.loads(JSON格式的字符串)：将JSON格式的字符串转为列表/字典；

"""


import json


# 定义一个列表，列表中的元素都是 dict
var01 = [{"name": "张三", "age": 18}, {"name": "李四", "age": 18}, {"name": "王五", "age": 18}]

# 将 dict 转为 JSON
var02 = json.dumps(var01, ensure_ascii=False)
print(f"将 dict 转为 JSON：var02 的类型为：{type(var02)}，var02 的内容为：{var02}")

# 将 JSON 格式的 String 转为 list（多个）
var03 = '[{"name": "张三", "age": 18}, {"name": "李四", "age": 18}, {"name": "王五", "age": 18}]'
var04 = json.loads(var03)
print(f"将 JSON 格式的 String 转为 list（多个）：var04 的类型为：{type(var04)}，var04 的内容为：{var04}")

# 将 JSON 格式的 String 转为 dict（单个）
var05 = '{"name": "张三", "age": 18}'
var06 = json.loads(var05)
print(f"将 JSON 格式的 String 转为 dict（单个）：var06 的类型为：{type(var06)}，var06 的内容为：{var06}")

