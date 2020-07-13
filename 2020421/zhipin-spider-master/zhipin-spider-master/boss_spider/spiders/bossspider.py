# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_splash import SplashRequest


class BossspiderSpider(scrapy.Spider):
    name = 'bossspider'
    
    def __init__(self, location=None, position=None, **kwargs):
        super().__init__(**kwargs)
        self.location = location
        self.position = position
        # 往splash服务器中发送的语句解释
        """
            # 关闭浏览器的私有模式 (匿名模式) 
            splash.private_mode_disable = false 
            # 配置request
            splash:on_request(function(request)
            # request中设置请求头
            request:set_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0")')
            end)
            # 请求的url
            url = args.url
            # 发起request请求
            assert(splash:go(url))
            # 等待5s
            assert(splash:wait(5))
            # 获取职位搜索输出框标签（元素）
            input_box = assert(splash:select(".ipt-search"))
            # 输入框获取焦点（相当与单击输入框）
            input_box:focus()
            # 往输入框中输入文字
            input_box:send_text("{self.position}")
            assert(splash:wait(0.5))
            # 按回车键，相当于按键盘的Enter按键
            input_box:send_keys("<Enter>")
            assert(splash:wait(10))
            # 返回加载完成之后的html页面
            return splash:html()
        """
        self.lua_script1 = f'''
        function main(splash, args)
            splash.private_mode_disable = false
            splash:on_request(function(request)
            request:set_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0")')
            end)
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(5))
            input_box = assert(splash:select(".ipt-search"))
            input_box:focus()
            input_box:send_text("{self.position}")
            assert(splash:wait(0.5))
            input_box:send_keys("<Enter>")
            assert(splash:wait(10))
            return splash:html()
        end
        '''
        self.lua_script2 = f'''
        function main(splash, args)
            splash.private_mode_disable = false
            splash:on_request(function(request)
            request:set_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0")')
            end)
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(5))
            return splash:html()
        end
        '''

    def start_requests(self):
        location = self.location.replace("'", "").strip()
        # 首页>>杭州地区
        aa = f"https://www.zhipin.com/{location}/"
        # 发起SplashRequest,
        # url为请求的url地址
        # callbank为请求完毕之后的回调函数，这个请求完毕后得到的是scrapy的响应对象
        # endpoint固定写法
        # args往splash服务器中传入的lua_source
        yield SplashRequest(url=aa,
                            callback=self.parse,
                            endpoint="execute",
                            args={'lua_source': self.lua_script1})

    # 解析函数
    def parse(self, response):
        # 获取响应html文件
        # resp_text = response.body.decode(response.encoding)
        # print(resp_text)
        for job in response.xpath("//div[@class='job-primary']"):
            yield {
                # 通过xpath解析获取第一条
                'job_name': job.xpath(".//span[@class='job-name']/a/text()").get(),
                'job_area': job.xpath(".//span[@class='job-area']/text()").get(),
                'company': job.xpath(".//div[@class='company-text']/h3/a/text()").get(),
                'salary': job.xpath(".//span[@class='red']/text()").get(),
                'required': job.xpath(".//div[@class='job-limit clearfix']/p/text()").get().replace('\n', ' '),
                # 通过xpaht解析获取所有
                'tags': job.xpath(".//div[@class='tags']/span[@class='tag-item']/text()").getall()
            }
        # 获取下一页的url地址后半部分
        next_page = response.xpath("//a[@class='next']/@href").get()
        if next_page:
            yield SplashRequest(url=f"https://www.zhipin.com{next_page}", # 拼接url,给splash服务器发起请求
                            callback=self.parse,
                            endpoint="execute",
                            args={'lua_source': self.lua_script2})
