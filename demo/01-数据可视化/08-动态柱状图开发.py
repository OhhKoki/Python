"""
    数据可视化开发：动态柱状图
"""


from pyecharts.charts import Bar, Timeline
from pyecharts.options import *


# 打开文件
file = open("/Users/terry/Documents/Workspace/PythonProjects/Python/data/经济.csv", "r", encoding="GB2312")

# 读取文件
data_lines = file.readlines()

# 关闭文件
file.close()

# 删除第一条数据
data_lines.pop(0)

# 将数据转为 dict
timeline = Timeline()
data_dict = {}

for line in data_lines:
    line = line.split(",")
    year = int(line[0])
    country = line[1]
    gdp = float(line[2])
    try:
        data_dict[year].append([country, gdp])
    except KeyError as e:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 根据年份进行排序
sorted_year_list = sorted(data_dict.keys())

for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份 GDP 排名为前 8 的国家
    year_data = data_dict[year][0: 8]
    x_data = []
    y_data = []
    # 遍历本年份 GDP 为前 8 的各个国家
    for country_gdp in year_data:
        # ['美国', '英国', '法国', '中国', '日本', '加拿大', '意大利', '印度']
        x_data.append(country_gdp[0])
        # [543300000000.0, 73233967692.0, 62225478000.0, 59716467625.0, 44307342950.0, 40461721692.0, 40385288344.0, 37029883875.0]
        y_data.append(country_gdp[1])
    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP（亿）", y_data, label_opts=LabelOpts(position="right"))
    # 反转 X 轴和 Y 轴
    bar.reversal_axis()
    # 设置全局数据
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    timeline.add(bar, str(year))

# 设置时间线自动播放
timeline.add_schema(
    # 自动播放的时间间隔
    play_interval=1000,
    # 是否显示时间线
    is_timeline_show=False,
    # 是否自动播放
    is_auto_play=True,
    # 是否循环播放
    is_loop_play=True
)

# 渲染图表
timeline.render()
