"""
    1、文件的编码
        01）什么是编码：
            编码是一种规则集合，记录了内容和二进制间的相互转换逻辑，最常用的是 UTF-8 编码；

        02）为什么编码：
            计算机只认识二进制，需要先将内容转为二进制才能保存到计算机。同时保存在计算机中的内容也是二进制的，需要通过编码转为自然语言。

    2、文件操作流程
        01）打开文件
            # mode 有三个模式 r（read）、w（write）、a（append）
            # open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
            file = open(file, mode, encoding)

        02）文件读写
            1、文件的写入
                file.write(字符内容)：将指定字符内容写入到指定文件中；

                对于内容的写入需要注意如下几个点：
                    01）如果要对文件写入时，open() 函数的 mode 需要为 w 或者 x 模式；
                    02）使用 w 模式打开文件时，如果文件不存在则创建文件，如果文件存在则清空文件中的内容；
                    03）write() 函数是将内容写入到内存的缓冲区中，需要使用 flush() 函数将缓冲区中的内容清空并写入磁盘；
                    04）close() 函数自带 flush() 函数的功能；

            2、文件的追加
                文件的追加操作和写入操作基本一样，只需要将 open() 函数的 mode 设置为 a 即可

                对于内容的追加需要注意如下几个点：
                    01）a 模式，不会创建文件；
                    02）a 模式，如果文件存在，则将内容追加到文件的末尾；

            3、文件的读取
                01）file.read(num)：读取指定字节的数据，参数缺省时则读取全部的数据，指针指向以读取数据的结尾；
                02）file.readline()：读取一行数据，指针指向以读取数据的结尾；
                03）file.readlines()：读取所有行数据，并以 list 列表并返回，指针指向以读取数据的结尾；
                04）for item in 文件对象：循环文件所有行，每次循环得到文件中的一行内容；

        03）关闭文件
            # 如果不调用 close() 函数，同时程序没有停止运行，那么这个文件将一直被 Python 占用
            file.close()

            另外可以通过 with open 语法创建一个可以自动关闭的文件，例如：
                with open(file, mode, encoding) as file:
                    for item in file:
                        print(item)

"""


# 1、打开文件
file = open("/Users/terry/Documents/Workspace/PythonProjects/Python/test.txt", "w", encoding="UTF-8")

# 写入文件
file.write("Hello World")

# 读取文件
# for item in file:
#     print(item)

# 关闭文件
file.close()

