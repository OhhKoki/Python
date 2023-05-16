"""
    1、怎么安装 PySpark 包？
        win：pip install pyspark
        mac：pip3 install pyspark -i https://mirrors.aliyun.com/pypi/simple/
"""

# 1、导包
from pyspark import SparkConf, SparkContext

# 2、创建 SparkConf 对象
conf = SparkConf().setMaster("local[*]").setAppName("test_pyspark_app")

# 3、创建 SparkContext 对象
context = SparkContext(conf=conf)

# 4、执行业务操作
print(context.version)

# 5、停止 Spark 程序
context.stop()


