# 1、导包
from pyspark import SparkConf, SparkContext

# 2、创建 SparkConf 对象
conf = SparkConf().setMaster("local[*]").setAppName("test_pyspark_app")

# 3、创建 SparkContext 对象
context = SparkContext(conf=conf)

# 4、数据输入：通过 parallelize 将 Python 的数据容器转为 RDD
container = [1, 2, 3, 4, 5]
rdd = context.parallelize(container)

def fun(data):
    return

rdd.map()

# 5、输出 RDD
print(rdd.collect())
