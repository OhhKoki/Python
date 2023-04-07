"""
    数据可视化开发：地图开发
"""


import json
from pyecharts.charts import Map
from pyecharts.options import *


# 打开文件
file = open("/Users/terry/Documents/Workspace/PythonProjects/Python/data/疫情.txt")

# 读取数据
data = file.read()

# 关闭文件
file.close()

# 将 JSON 转为 dict
data_dict = json.loads(data)

# 从 dict 中获取到省份数据
province_data_list = data_dict['areaTree'][0]['children']

# 遍历 province_data_list 列表，将每个省份的数据添加到元组中
data_list = []    # 绘图所需的元组

for province_data in province_data_list:
    province_name = province_data['name']                   # 省份名称
    province_name = province_name + "省"
    province_confirm = province_data['total']['confirm']    # 确诊人数
    data_list.append((province_name, province_confirm))

# 创建图表
map = Map()

# 添加数据
map.add("各省份确诊人数", data_list, "china")

# 全局配置项
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999", "color": "#FF9966"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#FF6666"},
            {"min": 100000, "label": "100000+", "color": "#990033"}
        ]
    )
)

# 图表渲染
map.render("全国疫情地图.html")
