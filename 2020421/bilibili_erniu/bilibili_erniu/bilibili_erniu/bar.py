from numbers import Number

from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline

from datetime import datetime
# import json
import csv

# import pandas as pd
# videos=pd.read_json('data.json') #Pandas库的read_json函数可用于将JSON文件读入为pandas DataFrame数据结构类型
# videos=json.loads(v)
csv_path='data5.csv'
year=[]
month=[]
day=[]
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
    # 使用列表推导式，将读取到的数据装进列表
    # data_list = [i for i in csv.reader(fp)]  # csv.reader 读取到的数据是list类型

# 读取json文件
# jsonPath = 'data.json'
# with open(jsonPath, 'r') as f:
#     videos = json.load(f)
# videos=data_list

# fi = open("data.json", 'r', encoding='utf-8')




# year = videos.values.year.astype('int')
# month = videos.month.astype('int')
# videos.day = videos.day.astype('int')
year = sorted(year)
print(year)

years = set(year)
months = []
# for year in years:
    # months.append(set(videos['year'].isin([year]).month))

timeline_2020 = Timeline()
for m in months[2]:
    bar = (
        Bar()
            .add_xaxis(list(videos[videos.year.isin([2020])][videos.month.isin([m])].day))
            .add_yaxis("播放量", list(videos[videos.year.isin([2020])][videos.month.isin([m])].play), yaxis_index=0, )
            .add_yaxis("评论数", list(videos[videos.year.isin([2020])][videos.month.isin([m])].comment), yaxis_index=1)
            .extend_axis(
            yaxis=opts.AxisOpts(
                name="评论数",
                type_="value",
                position="right",
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
            )
        )
            .set_global_opts(title_opts=opts.TitleOpts("山药村二牛{}年{}月视频播放量和评论数".format(2020, m)))
    )
    timeline_2020.add(bar, '{}月'.format(m))
