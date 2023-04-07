"""
    柱状图使用案例
"""


from pyecharts.charts import Bar
from pyecharts.options import LabelOpts


# 创建一个柱状图对象
bar = Bar()

# 给 X 轴添加数据
bar.add_xaxis(["中国", "美国", "英国"])

# 给 Y 轴添加数据（label_opts=LabelOpts(position="right") 的作用是将数据放在右侧）
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))

# 反转 X 轴 和 Y 轴
bar.reversal_axis()

# 图表渲染
bar.render("基础柱状图.html")
