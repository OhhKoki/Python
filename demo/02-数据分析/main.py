"""
    数据分析案例主业务逻辑
"""


from data_define import Record
from file_define import TextFileReader, JsonFileReader
from pyecharts.charts import Bar
from pyecharts.options import *


# 打开文件
text_file_reader = TextFileReader("/Users/terry/Documents/Workspace/PythonProjects/Python/data/销售.txt")
json_file_reader = JsonFileReader("/Users/terry/Documents/Workspace/PythonProjects/Python/data/销售的JSON.txt")

# 读取数据
jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 数据合并
all_data: list[Record] = jan_data + feb_data

# 数据计算
data_dict = {}
for record in all_data:
    current_date = record.date
    if record.date in data_dict.keys():
        # 当前日期已经存在，只需进行金额的累加
        data_dict[current_date] += record.money
    else:
        data_dict[record.date] = record.money

# 数据展示
bar = Bar()
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render()
