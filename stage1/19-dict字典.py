"""
    dict 字典的定义语法：
        变量名 = {key1: value1, key2: value2, key3: value3, ...}

        另外可以使用如下方式定义空列表
            变量名 = {}
            变量名 = dict()

    dict 字典的特点为：
        01）value 可以为任意类型，key 可以为除字典类型外的任意类型；
        02）key 不允许重续，如果存在两个重复的 key，内容会覆盖；
        03）字典没有下标索引，需要通过 key 检索 value；

    dict 字典的常用操作：
        01）字典[key] = value：新增元素；
        02）字典[key] = value：更新元素；
        03）字典.pop(key)：移除 key 对应的键值对，同时返回 key 对应的 value；
        04）字典.keys()：获取字典中所有的 key；
        05）len(字典)：获取字典中键值对数量；
        06）字典.clear()：清空字典；
"""


# 定义字典
# 注意：对于重复的 key，value 会覆盖；
# 注意：key 和 value 可以是任意类型；
var01 = {"name": "terry", "name": "tim", "age": 20, "weight": 55.5, 101: "序号"}
print(f"定义字典：{var01}")

# 通过 key 获取 value
var02 = var01["name"]
var03 = var01[101]
print(f"通过 key 获取 value：{var02}")
print(f"通过 key 获取 value：{var03}")

# 字典可以进行嵌套
var04 = {
    "张三": {
        "语文": 71,
        "数学": 72,
        "英语": 73
    },
    "李四": {
        "语文": 81,
        "数学": 82,
        "英语": 83
    },
    "王五": {
        "语文": 91,
        "数学": 92,
        "英语": 93
    }
}

print(f"学生的成绩信息为：{var04}")
print(f"张三的成绩信息为：{var04['张三']}")
print(f"张三语文的成绩为：{var04['张三']['语文']}")

"""
    dict 字典的常用操作：
        01）字典[key] = value：新增元素；
        02）字典[key] = value：更新元素；
        03）字典.pop(key)：移除 key 对应的键值对，同时返回 key 对应的 value；
        04）字典.keys()：获取字典中所有的 key；
        05）len(字典)：获取字典中键值对数量；
        06）字典.clear()：清空字典；
"""

# 定义字典
var05 = {"张三": 71, "李四": 72, "王五": 73}

# 新增元素
var05["赵六"] = 74
print(f"新增元素：{var05}")

# 更新元素
var05["赵六"] = 83
print(f"更新元素：{var05}")

# 字典.pop(key)：移除 key 对应的键值对，同时返回 key 对应的 value
var06 = var05.pop("赵六")
print(f"移除 key 时返回的 value 为：{var06}")
print(f"移除 key 后的字典内容为：{var05}")

# 字典.keys()：获取字典中所有的 key
var06 = var05.keys()
print(f"获取字典中所有的 key 值：{var06}")

# len(字典)：获取字典中键值对数量
var07 = len(var05)
print(f"获取字典中键值对数量：{var07}")

# 字典.clear()：清空字典
var05.clear()
print(f"清空字典：{var05}")

# 字典的遍历
var05 = {"张三": 71, "李四": 72, "王五": 73}

for item in var05:
    print(f"key 为：{item}，value 为：{var05[item]}")