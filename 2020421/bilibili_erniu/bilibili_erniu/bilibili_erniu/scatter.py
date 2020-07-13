from pyecharts.charts import Scatter
from pyecharts import options as opts
from pyecharts.charts import Bar
import csv
csv_path='data5.csv'
year=[]
month=[]
day=[]
play=[]
with open(csv_path,'r',encoding='utf8')as fp:
    reader = csv.DictReader(fp)
    year = [row['year'] for row in reader]
with open(csv_path, 'r', encoding='utf8')as fp:
    reader = csv.DictReader(fp)
    month = [row['month'] for row in reader]
with open(csv_path, 'r', encoding='utf8')as fp:
    reader = csv.DictReader(fp)
    day = [row['day'] for row in reader]
while '' in year:
    year.remove('')
while '' in month:
    month.remove('')
while '' in day:
    day.remove('')
year = list(map(int, year))
month = list(map(int, month))
day = list(map(int, day))
print(year)
print(month)
print(day)
play=[]
with open(csv_path,'r',encoding='utf8')as fp:
    reader = csv.DictReader(fp)
    play = [row['play'] for row in reader]
# c = (
#     Scatter()
#         .add_xaxis(list(range(2018,2021)))
#         .add_yaxis("播放量", list(play))
#         .set_global_opts(
#         title_opts=opts.TitleOpts(title="山药村二牛视频时长-播放量散点图"),
#         visualmap_opts=opts.VisualMapOpts(type_="size", max_=1000000, min_=27000),
#     )
# )

# //导入柱状图-Bar
# # from pyecharts import Bar
# # //设置行名
columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# # //设置数据
# # data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
# # data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# # //设置柱状图的主标题与副标题
# title="柱状图"
# bar = Bar()
# # //添加柱状图的数据及配置项
# bar.add("降水量", columns, year, mark_line=["average"], mark_point=["max", "min"])
# bar.add("蒸发量", columns, day, mark_line=["average"], mark_point=["max", "min"])
# # //生成本地文件（默认为.html文件）
# bar.render()


# # //导入饼图Pie
# from pyecharts.charts import Pie
# # //设置主标题与副标题，标题设置居中，设置宽度为900
# pie = Pie("饼状图", "一年的降水量与蒸发量")
# # //加入数据，设置坐标位置为【25，50】，上方的colums选项取消显示
# pie.add("降水量", columns, year ,center=[25,50],is_legend_show=False)
# # //加入数据，设置坐标位置为【75，50】，上方的colums选项取消显示，显示label标签
# pie.add("蒸发量", columns, play ,center=[75,50],is_legend_show=False,is_label_show=True)
# # //保存图表
# pie.render()
#
# from pyecharts import Line
# line = Line("折线图","一年的降水量与蒸发量")
# //is_label_show是设置上方数据是否显示
# line.add("降水量", columns, data1, is_label_show=True)
# line.add("蒸发量", columns, data2, is_label_show=True)
# line.render()
#
# from pyecharts import Radar
# radar = Radar("雷达图", "一年的降水量与蒸发量")
# //由于雷达图传入的数据得为多维数据，所以这里需要做一下处理
# radar_data1 = [[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]]
# radar_data2 = [[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]]
# //设置column的最大值，为了雷达图更为直观，这里的月份最大值设置有所不同
# schema = [
#     ("Jan", 5), ("Feb",10), ("Mar", 10),
#     ("Apr", 50), ("May", 50), ("Jun", 200),
#     ("Jul", 200), ("Aug", 200), ("Sep", 50),
#     ("Oct", 50), ("Nov", 10), ("Dec", 5)
# ]
# //传入坐标
# radar.config(schema)
# radar.add("降水量",radar_data1)
# //一般默认为同一种颜色，这里为了便于区分，需要设置item的颜色
# radar.add("蒸发量",radar_data2,item_color="#1C86EE")
# radar.render()
#
# from pyecharts import Scatter
# scatter = Scatter("散点图", "一年的降水量与蒸发量")
# //xais_name是设置横坐标名称，这里由于显示问题，还需要将y轴名称与y轴的距离进行设置
# scatter.add("降水量与蒸发量的散点分布", data1,data2,xaxis_name="降水量",yaxis_name="蒸发量",
#             yaxis_name_gap=40)
# scatter.render()
#
# from pyecharts import Grid
# //设置折线图标题位置
# line = Line("折线图","一年的降水量与蒸发量",title_top="45%")
# line.add("降水量", columns, data1, is_label_show=True)
# line.add("蒸发量", columns, data2, is_label_show=True)
# grid = Grid()
# //设置两个图表的相对位置
# grid.add(bar, grid_bottom="60%")
# grid.add(line, grid_top="60%")
# grid.render()
#
# from pyecharts import Overlap
# overlap = Overlap()
# bar = Bar("柱状图-折线图合并", "一年的降水量与蒸发量")
# bar.add("降水量", columns, data1, mark_point=["max", "min"])
# bar.add("蒸发量", columns, data2, mark_point=["max", "min"])
# overlap.add(bar)
# overlap.add(line)
# overlap.render()