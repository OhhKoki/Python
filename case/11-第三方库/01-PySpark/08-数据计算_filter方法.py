# 1、导包
from pyspark import SparkConf, SparkContext

# 2、创建 SparkConf 对象
conf = SparkConf().setMaster("local[*]").setAppName("test_pyspark_app")

# 3、创建 SparkContext 对象
context = SparkContext(conf=conf)

# 4、数据输入：通过 parallelize 将 Python 的数据容器转为 RDD
container = [1, 2, 3, 4, 5, 6]
rdd = context.parallelize(container)
# 需求：只想要偶数的数字，奇书的丢弃
rdd_filter = rddReduceByKey = rdd.filter(lambda x: x % 2 == 0)

# 5、输出 RDD
print(f"value is: {rdd_filter.collect()}")
