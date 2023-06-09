"""
    1、什么是包
        从物理上看，包就是一个文件夹，该文件夹在包含一个 __init__.py 的文件，该文件可以用包含多个模块文件；
        从逻辑上看，包本质依然是一个模块；

    2、包的作用
        当我们的模块文件越来越多，包可以帮助我们管理这些模块，包的作用就是包含多个模块，但包的本质依然是模块；

    3、导入包
        import 包
        import 包.模块
        import 包.模块.类
        import 包.模块.类.函数
        ...

        from 包 import 模块
        from 包 import 模块.类
        from 包 import 模块.类.方法
        ...

    4、安装第三方包
        语法：pip install 包名称
        案例：pip install numpy

        mac 环境为：
            语法：pip3 install 包名
            案例：pip3 install pyecharts
"""