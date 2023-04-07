"""
    地图使用案例
"""


from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts


# 创建图表
map = Map()

# 准备数据
data = [
    ("湖北省", 199),
    ("河南省", 299),
    ("湖南省", 399),
    ("广东省", 499),
    ("台湾省", 499),
]

# 添加数据
map.add("测试地图", data, "china")

# 全局配置项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        # 设置地图显示颜色
        is_show=True,
        # 设置开启手动设置地图颜色范围
        is_piecewise=True,
        # 地图颜色范围配置信息
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#CCDDFF"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#CCAAFF"}
        ]
    )
)

# 图表渲染
map.render()
