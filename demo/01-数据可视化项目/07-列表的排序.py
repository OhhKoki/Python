# 定义一个列表
var01 = [["a", 30], ["b", 60], ["c", 40]]


def choose_sort_key(element):
    return element[1]


# 基于函数名进行排序
var01.sort(key=choose_sort_key, reverse=True)
print(var01)


# 定义一个列表
var02 = [["a", 30], ["b", 60], ["c", 40]]

# 基于匿名进行排序
var02.sort(key=lambda element: element[1], reverse=False)
print(var02)








