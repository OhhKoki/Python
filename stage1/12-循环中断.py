"""
    无论是 while 循环还是 for 循环，都是在重复性的执行某些操作。那么怎么提前退出退出循环呢？
        continue：跳过本轮循环，直接进入下一轮循环
        break：结束循环
"""


# continue 的使用案例
for x in range(2):
    print("code one")
    for y in range(2):
        print("code two")
        continue
        print("code three")
    print("code four")
    print("-----")


# break 的使用案例
for x in range(2):
    print("code one")
    for y in range(10):
        print("code two")
        break
        print("code three")
    print("code four")
    print("-----")

