# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliErniuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    aid = scrapy.Field()
    bvid = scrapy.Field()
    comment = scrapy.Field()
    created_time = scrapy.Field()
    length = scrapy.Field()
    play = scrapy.Field()
    cid = scrapy.Field()
    time = scrapy.Field()
    date = scrapy.Field()
    hour_min = scrapy.Field()
    year = scrapy.Field()
    month = scrapy.Field()
    day = scrapy.Field()


class ErniuBulletChatItem(scrapy.Item):
    cid = scrapy.Field()
    content = scrapy.Field()
