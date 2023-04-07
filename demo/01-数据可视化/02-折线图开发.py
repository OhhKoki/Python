"""
    数据可视化开发：折线图开发
"""


import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts


# 打开文件
f_us = open("/Users/terry/Documents/Workspace/PythonProjects/Python/data/美国.txt", "r", encoding="UTF-8")
f_jp = open("/Users/terry/Documents/Workspace/PythonProjects/Python/data/日本.txt", "r", encoding="UTF-8")
f_in = open("/Users/terry/Documents/Workspace/PythonProjects/Python/data/印度.txt", "r", encoding="UTF-8")

# 读取数据
us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()

# 关闭文件
f_us.close()
f_jp.close()
f_in.close()

# 去掉不符合 JSON 规范的开头部分
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

# 去掉不符合 JSON 规范的结尾部分
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# 将 JSON 字符串转为 dict
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取 trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据，用于 X 轴（本案例只展示 2020 年的数据。即：到下标 314 结束）
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获取
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 创建图表
line = Line()

# 添加 X 轴数据
line.add_xaxis(us_x_data)    # 注意 X 轴的数据是共用的，所以设置一份就行了

# 添加 Y 轴数据
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局选项
line.set_global_opts(
    # 设置标题
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")
)

# 渲染图表
line.render()


