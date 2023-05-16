# 1、导包
from pyspark import SparkConf, SparkContext

# 2、创建 SparkConf 对象
conf = SparkConf().setMaster("local[*]").setAppName("test_pyspark_app")

# 3、创建 SparkContext 对象
context = SparkContext(conf=conf)

# 4、数据输入：通过 parallelize 将 Python 的数据容器转为 RDD
container = ["i am terry", "who am i", "i am terry"]
rdd = context.parallelize(container)
# 将 RDD 中的每个单词都提取出来
rddMap = rdd.flatMap(lambda x: x.split(" "))
rddFlatMap = rdd.flatMap(lambda x: x.split(" "))

# 5、输出 RDD
print(f"rddMap value is: {rddMap.collect()}")
print(f"rddFlatMap value is: {rddFlatMap.collect()}")
