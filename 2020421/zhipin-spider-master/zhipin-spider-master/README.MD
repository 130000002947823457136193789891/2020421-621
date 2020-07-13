## usage

### 1.运行容器

 1. 调出命令终端：

    1.1win + r
    1.2 输入cmd ,按回车

2. 启动splash服务，如果第一次启动，会从官方拉splash镜像，耗时较长

```bash
scrapy-splash，这个容器是用来模拟浏览器的请求解析页面:
docker run -it -p 8050:8050 --rm scrapinghub/splash

```

 	3. 验证：在浏览器中输入：<http://127.0.0.1:8050/>
     ![1590656832527](C:\Users\tiddler66\AppData\Roaming\Typora\typora-user-images\1590656832527.png)

### 2.爬取命令行示例

比如爬取杭州的java职位信息：
在运行命令时需要切换到项目内部中：

![1590657427980](C:\Users\tiddler66\AppData\Roaming\Typora\typora-user-images\1590657427980.png)

```bash
scrapy crawl bossspider -a location='hangzhou' -a position='java'
```

如果想要输出到文件：

-a 表示传入参数 

-o 表示向外输出

```bash
scrapy crawl bossspider -a location='hangzhou' -a position='java' -o data.csv
```

### 注意事项
注意修改settings.py文件里面的mongoDB配置。