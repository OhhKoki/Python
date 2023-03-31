"""
    list 列表的定义语法：
        变量名 = [元素1, 元素2, 元素3, ...]

        另外可以使用如下方式定义空列表
            变量名 = []
            变量名 = list()

        list 的特点为：有序，又重复，类型不限制
"""

# list 可以包含重复的元素，元素的类型没有限制
user_info = ["terry", "terry", 18, 50.5, ["篮球", "足球", "排球"]]

for item in user_info:
    print(item)

print("-----")

# list 中的每个元素，都存在一个下标索引，从零开始，通过该索引，可以从 list 获取元素
for item in range(5):
    print(user_info[item])

print("-----")

# 这个索引，甚至还可以反向的，最后一个元素的索引为 -1，倒数第二个为 -2，依此类推
for item in range(-1, -6, -1):
    print(f"当前索引为：{item}，索引位置处的元素为：{user_info[item]}")

print("-----")

# 通过二维数组的形式，可以获取子列表中的元素
print(user_info[4][1])

print("-----")

"""
    list 的常用方法
        01）列表.index(element)：查找元素在列表内的下标（第一个），找不到则报错；
        02）列表[index] = 值：对列表指定位置处的元素进行重新赋值；
        03）列表.insert(index,element)：在列表的指定索引前，插入指定元素；
        04）列表.append(element)：将指定元素，追加到列表的尾部；
        05）列表.extend(element)：将其他数据容器的元素取出，然后依次追加到当前容器尾部；
        06）列表.pop(index)：删除指定索引处的元素；
        07）del 列表[index]：删除指定索引处的元素；
        08）列表.remove(element)：删除指定元素（注意：遍历列表，删除第一个匹配的元素！！！）
        09）列表.count(element)：统计指定元素在列表内的数量；
        10）len(列表)：获取列表中元素的个数；
        11）列表.clear()：清空列表；
        
"""
# 查找元素索引
print(f"terry 在 list 中的索引位置为：{user_info.index('terry')}")

# 修改列表指定索引处的元素进行重新赋值
user_info[1] = "tim"
user_info[-2] = 51.5
print(f"对 list 索引为 1 处的元素进行重新赋值：{user_info}")

# 在列表的指定索引前，插入指定元素（指定索引前！！！！！）
user_info.insert(-1, ["电影", "音乐", "小说"])
print(f"在列表的指定位置，插入指定元素：{user_info}")

# 将指定元素，追加到列表的尾部
user_info.append("dept101")
print(f"将指定元素，追加到列表的尾部：{user_info}")

# 将其他数据容器的元素取出，然后依次追加到当前容器尾部
cities = ["北京", "上海", "广州"]
user_info.extend(cities)
print(f"将其他数据容器的元素取出，然后依次追加到当前容器尾部：{user_info}")

# 删除元素：pop
user_info.pop(1)
print(f"通过 pop 删除指定索引处的元素：{user_info}")

# 删除元素：del
del user_info[-1]
print(f"通过 del 删除指定索引处的元素：{user_info}")

# 删除元素：remove（注意：遍历列表，删除第一个匹配的元素！！！）
user_info.remove("上海")
print(f"通过 remove 删除指定的元素：{user_info}")

# 统计指定元素在列表内的数量
count = user_info.count("terry")
print(f"统计 terry 这个在列表中的个数：{count}")

# 统计指定元素在列表内的数量；
count = len(user_info)
print(f"列表中元素的个数位：{count}")

# 清空列表
user_info.clear()
print(f"清空列表：{user_info}")

print("-----")

"""
    使用 for 或者 while 对 list 进行遍历
"""
user_info = ["terry", 18, 50.5, ["篮球", "足球", "排球"]]

for item in user_info:
    print(item)

print("-----")

index = 0

while index < len(user_info):
    print(user_info[index])
    index += 1

