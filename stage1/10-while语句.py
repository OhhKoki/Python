"""
    2）while 语句
        while 条件:
            条件满足时做的事情
"""


# 练习：0-100 的累加
i = 0
sum = 0
while i <= 100:
    i += 1
    sum += i
    if i == 100:
        print(f"当前 sum 的值为：{sum}")


# 练习：猜数字游戏
import random    # 导入类
randomNum = random.randint(1,100)    # 获取一个 1-100 之间的随机数
flag = True
while flag:
    guessNum = int(input("请输入你猜的数字：\n"))
    if guessNum > randomNum:
        print("你猜大了")
    elif guessNum < randomNum:
        print("你猜小了")
    else:
        print("你猜对了")
        flag = False


# 练习：乘法口诀表
row = 1

while row <= 9:
    column = 1
    while column <= row:
        print(f"{column} * {row} = {column * row}\t", end='')
        column += 1
    row += 1
    print()

