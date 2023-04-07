"""
    柱状图使用案例
"""


from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType


# 创建一个柱状图对象
bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

# 创建一个柱状图对象
bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [40, 50, 20], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

# 创建一个柱状图对象
bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [50, 40, 60], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 创建一个时间线对象
# timelime = Timeline()
timelime = Timeline({"theme": ThemeType.CHALK})    # 设置时间线的主题
# 在时间线对象上添加柱状图对象
timelime.add(bar1, "点1")
timelime.add(bar2, "点2")
timelime.add(bar3, "点3")
# 时间线对象自动播放
timelime.add_schema(
    # 自动播放的时间间隔
    play_interval=1000,
    # 是否显示时间线
    is_timeline_show=True,
    # 是否自动播放
    is_auto_play=True,
    # 是否循环播放
    is_loop_play=True
)

# 使用时间线对象时，需要使用时间线对象进行渲染
timelime.render("时间线柱状图.html")
