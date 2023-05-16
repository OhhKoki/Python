# 1、导包
from pyspark import SparkConf, SparkContext

# 2、创建 SparkConf 对象
conf = SparkConf().setMaster("local[*]").setAppName("test_pyspark_app")

# 3、创建 SparkContext 对象
context = SparkContext(conf=conf)

# 4、数据输入
# 读取到多行句子
rdd_line = context.textFile("/Users/terry/Documents/Workspace/PythonProjects/Python/data/文章.txt")
# 把每一行句子，根据空格拆分成单词
rdd_word = rdd_line.flatMap(lambda line: line.split(" "))
# 单词转为小写
rdd_word_lower = rdd_word.map(lambda word: word.lower())
# 把每个单词转为二元元组，便于统计，结构为：[('his', 1), ('partner', 1)]
rdd_word_tuple = rdd_word_lower.map(lambda word: (word, 1))
# 分组统计
rdd_word_reduce = rdd_word_tuple.reduceByKey(lambda x, y: x + y)

# 5、输出 RDD
print(f"rddReduceByKey value is: {rdd_word_reduce.collect()}")
