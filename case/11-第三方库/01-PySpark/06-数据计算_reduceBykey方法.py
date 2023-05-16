# 1、导包
from pyspark import SparkConf, SparkContext

# 2、创建 SparkConf 对象
conf = SparkConf().setMaster("local[*]").setAppName("test_pyspark_app")

# 3、创建 SparkContext 对象
context = SparkContext(conf=conf)

# 4、数据输入：通过 parallelize 将 Python 的数据容器转为 RDD
container = [('Math', 85), ('English', 82), ('Math', 93), ('English', 82), ('Math', 79), ('English', 76)]
rdd = context.parallelize(container)
# 需求：按照学科进行分组，然后统计各个学科的总成绩
rddReduceByKey = rdd.reduceByKey(lambda x,y: x + y)

# 5、输出 RDD
print(f"rddReduceByKey value is: {rddReduceByKey.collect()}")
