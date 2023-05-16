"""
    通过 Python 连接到 Mysql 数据库：
        1、使用哪个第三方库来操作 Mysql，如果安装？
            1）第三方库：pymysql
            2）如何安装：pip install pymysql，mac os 为：pip3 install pymsql

        2、如何获取连接对象？
            1）导包：from pymysql import Connection
            2）创建连接对象：Connection(主机, 端口, 账号, 密码)
            3）关闭连接对象：连接对象.close()

        3、如何执行 SQL 语句？
            1）通过 Connection 对象设置要操作的数据库：conn.select_db("test")
            2）通过连接对象得到一个游标对象：cursor = conn.cursor()
            3）游标对象执行 SQL 语句：cursor.execute("create table")
"""


# 1、导入包
from pymysql import Connection


# 2、构建数据库连接对象
conn = Connection(
    host="150.158.14.200",
    port=3306,
    user="admin",
    password="root",
    autocommit=True    # 自动提交，不需要 conn.commit()
)

# 3、设置要操作的 DB
conn.select_db("ruoyi-vue")

# 4、获取游标对象
cursor = conn.cursor()

# 5、执行非查询性质的 SQL 语句
# createSql = "create table student (name char(20), age int)"
# cursor.execute(createSql)
# insertSql = "insert into student values('terry', 20)"
# cursor.execute(insertSql)
# conn.commit()

# 5、执行查询性质的 SQL 语句
selectSql = "select * from student"
cursor.execute(selectSql)
result: tuple = cursor.fetchall()

for line in result:
    print(line)

# 6、关闭连接
conn.close()
