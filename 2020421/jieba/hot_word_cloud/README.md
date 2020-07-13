# 对杭州地区，最近正在播放的电影，对用户电影评论信息，进行词云展示
  * 1、分析杭州现在正在上映的电影，爬取网址：https://movie.douban.com/nowplaying/hangzhou/
```
[{'id': '30318116', 'name': '利刃出鞘'},
{'id': '1292063', 'name': '美丽人生'},
{'id': '25842038', 'name': '理查德·朱维尔的哀歌'},
{'id': '26871938', 'name': '灭绝'},
{'id': '33424345', 'name': '紫罗兰永恒花园外传：永远与自动手记人偶'},
{'id': '26984189', 'name': '坂本龙一：终曲'}]
```
  * 2、获取正在上映电影的评论，翻阅10页，每页显示20条（代码中只获取的上面其中一个电影）
  * 3、将上面的评论拼接在一起
  * 4、对评论数据进行处理
    * 去掉标点符号(使用规则引擎知识点)
    * 进行分词（使用自然处理技术<NLP>分词的知识点）
    * 去掉停用词（文件加载知识点、Python语法知识点）
    * 对最后的词进行单词排序（Python语法知识点）
    * 将词和词的频率次数（频率次数越大，词越大）在图片上显示（词云显示的Python库WordCloud使用）

# 相关资料参考
 * 分词工具汇总：https://blog.csdn.net/fendouaini/article/details/82027310
 * Unofficial Windows Binaries for Python Extension Packages
    * https://www.lfd.uci.edu/~gohlke/pythonlibs/
 * install and publish Python packages with the Python Package Index
    * https://pypi.org/
