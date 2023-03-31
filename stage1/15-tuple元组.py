"""
    什么是 tuple：只读的 list 就是 tuple

    tuple 的定义语法：
        变量名 = (元素1, 元素2, 元素3, ...)

        可以通过如下当时定义空元组：
            变量名 = ()
            变量名 = tuple()

    tuple 的常用方法：
        元组.index(element)：查找指定元素，如果元素在元组中存在则返回其索引，不存在则报错；
        元组.count(element)：统计指定元素在当前元组中出现的次数；
        len(元组)：返回指定元组中元素的个数；
"""


user_info = ("terry", 18, 50.5, ("篮球", "足球", "排球"))

for item in user_info:
    print(item)

# user_info[0] = "tim"

# 元组.index(element)：查找指定元素，如果元素在元组中存在则返回其索引，不存在则报错
index = user_info.index(50.5)
print(f"获取元素索引：{index}")

# 元组.count(element)：统计指定元素在当前元组中出现的次数
count = user_info.count(("篮球", "足球", "排球"))     # 查找子元素时，子元素必须完全一样才会视为同一个元素！！！
print(f"统计元素出现的次数：{count}")

# len(元组)：返回指定元组中元素的个数
count = len(user_info)
print(f"获取元组中元素的总个数：{count}")

# 元组中的列表，可以进行修改！！！
user_info = ("terry", 18, 50.5, ["篮球", "足球", "排球"])
user_info[3][1] = "棒球"
print(f"元组中的列表，可以进行修改：{user_info}")