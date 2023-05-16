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
    return data * 10


# 需求：每个数字都变大 10 倍，然后加 5
# 可以通过链式调用的方式多次调用 map 方法，返回一个新的 RDD 对象（原始的 RDD 对象内容不变！！！）
rddMap = rdd.map(fun).map(lambda x: x + 5)

# 5、输出 RDD
print(f"value is: {rddMap.collect()}")
