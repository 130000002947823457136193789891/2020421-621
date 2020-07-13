# -*- coding: utf-8 -*-
import scrapy
import json
from bilibili_erniu.items import BilibiliErniuItem, ErniuBulletChatItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    # start_urls = ['http://bilibili.com/']

    def start_requests(self):
        base_url = 'https://api.bilibili.com/x/space/arc/search?mid=113362335&ps=30&tid=0&pn={}&keyword=&order=pubdate&jsonp=jsonp'
        headers = self.settings.get('DEFAULT_REQUEST_HEADERS')
        for pn in range(1, 10):
            url = base_url.format(pn)
            yield scrapy.Request(url=url, headers=headers, callback=self.parse_video_info)

    def parse_video_info(self, response):
        detail = json.loads(response.text)
        headers = self.settings.get('DEFAULT_REQUEST_HEADERS')
        for info in detail.get('data').get('list').get('vlist'):
            item = BilibiliErniuItem()
            item['title'] = info.get('title')
            item['aid'] = info.get('aid')
            item['bvid'] = info.get('bvid')
            item['comment'] = info.get('comment')
            item['created_time'] = info.get('created')
            item['length'] = info.get('length')
            item['play'] = info.get('play')
            cid_url = 'https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp'.format(item['bvid'])
            yield scrapy.Request(url=cid_url, headers=headers, meta={'item': item}, callback=self.get_bullet_chat_url)

    def get_bullet_chat_url(self, response):
        detail = json.loads(response.text)
        headers = self.settings.get('DEFAULT_REQUEST_HEADERS')
        item = response.meta['item']
        cid = detail.get('data')[0].get('cid')
        item['cid'] = cid
        bullet_chat_url = 'http://comment.bilibili.com/{}.xml'.format(cid)
        yield scrapy.Request(url=bullet_chat_url, headers=headers, meta={'cid': cid}, callback=self.parse_bullet_chat)
        yield item

    def parse_bullet_chat(self, response):
        sel = scrapy.Selector(response)
        item = ErniuBulletChatItem()
        item['cid'] = response.meta['cid']
        item['content'] = sel.xpath('//d//text()').extract()
        yield item

    def parse(self, response):
        pass
