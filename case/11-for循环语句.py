"""
    for 语句：
        for 临时变量 in 序列:
            循环满足条件时执行的代码
"""


var01 = "Hello World"

for item in var01:
    print(item)

print("-----")

"""
    range() 函数：
        range(num)：获取一个 [0,num) 的数字序列；
        range(num1,num2)：获取一个 [num1,num2) 的数字序列；
        range(num1,num2,step)：获取一个 [num1,num2) 的数字序列，其中数字之间的步长，以 step 为准；
"""


# for 与 range 配合使用
for item in range(10):
    print(item)

print("-----")

for item in range(5, 10):
    print(item)

print("-----")

for item in range(5, 10, 2):
    print(item)

print("-----")

for i in range(1, 10):
    j = 1
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i} \t", end='')
        j += 1
    i += 1
    print()
