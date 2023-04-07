"""
    折线图的使用案例
"""


from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts


# 创建一个折线图对象
line = Line()

# 给折线图对象添加 X 轴的数据
line.add_xaxis(["中国", "美国", "英国"])

# 给折线图对象添加 Y 轴的数据
line.add_yaxis("GDP", [30, 20, 10])

# 设置全局配置项（标题、图例、工具箱等，这是通用配置，不管什么图表都有的配置项）
line.set_global_opts(
    # 设置标题
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    # 设置图列
    legend_opts=LegendOpts(is_show=True),
    # 设置工具箱
    toolbox_opts=ToolboxOpts(is_show=True),
    # 设置视觉映射
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 通过 render() 方法将代码生成图像
line.render()
