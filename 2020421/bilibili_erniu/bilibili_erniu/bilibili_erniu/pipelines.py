# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from items import BilibiliErniuItem, ErniuBulletChatItem


class BilibiliErniuPipeline(object):
    def __init__(self):
        self.dirs = 'E:\\bili.csv'
        # self.dirs = 'E:\\dataset\\bilibili_erniu\\video_113362335.csv'
        if not os.path.exists(self.dirs):
            with open(self.dirs, 'w', encoding='utf-8')as fp:
                fp.write('title|aid|bvid|comment|created_time|length|play|cid|time|date|hour_min|year|month|day\n')
        self.buttet_chat_dir = 'E:\\bili'
        # self.buttet_chat_dir = 'E:\\dataset\\bilibili_erniu\\buttet_chat_113362335'
        if not os.path.exists(self.buttet_chat_dir):
            os.makedirs(self.buttet_chat_dir)

    def process_item(self, item, spider):
        if isinstance(item, BilibiliErniuItem):
            with open(self.dirs, 'a', encoding='utf-8') as fp:
                fp.write(item['title'] + '|' + str(item['aid']) + '|' + item['bvid'] + '|' + str(item['comment']) + '|' + str(item['created_time']) + '|' + item['length'] + '|' + str(item['play']) + '|' + str(item['cid']) + '|' + str(item['time']) + '|' + str(item['date']) + '|' + str(item['hour_min']) + '|' + str(item['year']) + '|' + str(item['month']) + '|' + str(item['day']) + '\n')
            return item
        else:
            filename = str(item['cid']) + '.csv'
            if not os.path.exists(self.buttet_chat_dir + '\\' + filename):
                with open(self.buttet_chat_dir + '\\' + filename, 'w', encoding='utf-8')as fp:
                    fp.write('content' + '\n')
                    for content in item['content']:
                        fp.write(content + '\n')
            return item


