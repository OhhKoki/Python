"""
    1、通过 SparkContext 对象的 parallelize 成员方法，可以将 Python 的数据容器对象转为 PySpark 的 RDD 对象
        1）Python 的数据容器有：list、tuple、set、dict、str
        2）字符串会被拆分成一个个的字符，存入 RDD，dict 仅有 key 会被存入 RDD 对象

    2、通过 SparkContext 对象的 parallelize 成员方法，可以将文本文件转为 PySpark 的 RDD 对象

"""

# 1、导包
from pyspark import SparkConf, SparkContext

# 2、创建 SparkConf 对象
conf = SparkConf().setMaster("local[*]").setAppName("test_pyspark_app")

# 3、创建 SparkContext 对象
context = SparkContext(conf=conf)

# 4.1 数据输入：通过 parallelize 将 Python 的数据容器转为 RDD
listData = [1, 2, 3]
tupleData = (1, 2, 3)
setData = {1, "b", True}
dictData = {"name": "terry", "age": 18}
strData = "hello world"

rddList = context.parallelize(listData)
rddTuple = context.parallelize(tupleData)
rddSet = context.parallelize(setData)
rddDict = context.parallelize(dictData)
rddStr = context.parallelize(strData)

# 4.2 数据输入：读取数据文件
rddText = context.textFile("/Users/terry/Documents/Workspace/PythonProjects/Python/data/销售.txt")

# 5、输出 RDD，如果想要查看 RDD 里面有什么内容，需要使用 collect() 方法
print(rddList.collect())
print(rddTuple.collect())
print(rddSet.collect())
print(rddDict.collect())
print(rddStr.collect())
print(rddText.collect())
