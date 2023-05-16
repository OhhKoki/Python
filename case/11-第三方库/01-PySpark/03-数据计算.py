"""
    1、PySpark 的数据计算，都是基于 RDD 对象来进行的，那么如何计算呢？
        RDD 对象中内置了丰富的成员方法（算子），通过这些方法进行计算

    2、常用的方法有哪些？
        map、flatMap、reduceByKey、filter、distinct、sortBy

    3、方法对应的功能是什么？
        map：将 RDD 数据一条条处理（传入一个匿名函数，该函数即为处理逻辑），返回新的 RDD 对象；
            案例：rdd.map(fun).map(lambda x: x + 5)

        flatMap：对 RDD 对象执行 map 操作，然后进行解除嵌套操作；
            案例：rdd.flatMap(lambda x: x.split(" "))

        reduceByKey：针对 KV 型的 RDD，自动按照 key 分组，然后根据你提供的聚合逻辑，完成组内数组（value）的聚合操作；
            1）在 Spark 中，KV 型的 RDD 指的是二元元组，例如：tupleData = [('a', 1), ('a', 2), ('b', 1), ('b', 2)]；
            2）在 Spark 中，对于二元元组的第一个元素，称为 key，例如上面的这个 a 和 b；
            3）聚合是针对二元元组的 value 进行聚合；
            4）总结起来就是针对二元元组，根据 key 先进行分组，分组完之后，在对 value 进行聚合，聚合的逻辑由你提供；
            5）注意：进行聚合的函数，只负责对 value 进行聚合，不需要理会分组，分组是根据 key 自动进行的；
            案例：rdd.reduceByKey(lambda x,y: x + y)

        filter：过滤想要的数据（不满足条件的数据去掉，只保留满足条件的数据）；
            和 map 的操作有些类似，将 RDD 数据一条条处理，对每一条数据进行判断是否符合指定的条件，符合返回 True 进行保留，不符合返回 False 会丢弃；
            案例：rdd.filter(lambda x: x % 2 == 0)

        distinct：对 RDD 数据进行去重；
            案例：rdd.distinct()

        sortBy：对 RDD 数据，基于你传入的排序逻辑进行排序；
            主要有三个参数：
                function：传入一个函数，该函数需要返回一个数据，用于告知按照 RDD 哪个数据就行排序，例如 lambda x: x[1] 表示按照 RDD 的第二列元素进行排序；
                ascending：True 表示升序，False 表示降序；
                numPartitions：用多少分区排序（例如 1 表示一个分区，1 个分区则全局有序）；
            案例：rdd_word_reduce.sortBy(lambda x: x[1], ascending=False, numPartitions=1)

"""


