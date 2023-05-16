"""
    1、PySpark 的数据计算，都是基于 RDD 对象来进行的，那么如何计算呢？
        RDD 对象中内置了丰富的成员方法（算子），通过这些方法进行计算

    2、常用的方法有哪些？
        map、flatMap、reduceByKey、filter、distinct、sortBy

    3、方法对应的功能是什么？
        map：将 RDD 数据一条条处理（传入一个匿名函数，该函数即为处理逻辑），返回新的 RDD 对象；
        flatMap：对 RDD 对象执行 map 操作，然后进行解除嵌套操作；

"""
